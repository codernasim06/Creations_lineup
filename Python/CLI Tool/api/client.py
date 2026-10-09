"""Asynchronous GitHub API client used by the CLI.

The implementation uses Python's standard library HTTP client in a worker
thread, so the project does not require an additional HTTP dependency.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class GitHubAPIError(RuntimeError):
    """Raised when GitHub cannot satisfy an API request."""


class GitHubAsyncClient:
    """Small async wrapper around the GitHub REST API."""

    BASE_URL = "https://api.github.com"
    API_VERSION = "2022-11-28"

    def __init__(self, token: Optional[str] = None, timeout: float = 20.0) -> None:
        self.token = token
        self.timeout = timeout
        self._closed = False

    async def close(self) -> None:
        """Close the client.

        Requests use short-lived standard-library connections, so there is no
        persistent session to dispose of. This method exists for a clean CLI
        lifecycle and compatibility with the entry point.
        """

        self._closed = True

    async def _request(
        self,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if self._closed:
            raise GitHubAPIError("GitHub client is already closed")

        url = f"{self.BASE_URL}{path}"
        if params:
            url = f"{url}?{urlencode(params)}"

        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": self.API_VERSION,
            "User-Agent": "githubinfo-cli",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        request = Request(url, headers=headers, method="GET")
        return await asyncio.to_thread(self._request_sync, request)

    def _request_sync(self, request: Request) -> Any:
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            try:
                details = json.loads(exc.read().decode("utf-8"))
                message = details.get("message", str(exc))
            except (ValueError, UnicodeDecodeError):
                message = str(exc)
            raise GitHubAPIError(f"GitHub API error ({exc.code}): {message}") from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise GitHubAPIError(f"Unable to reach GitHub: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise GitHubAPIError("GitHub returned invalid JSON") from exc

    async def get_profile(self, username: str) -> Dict[str, Any]:
        """Return a normalized profile payload."""

        return await self._request(f"/users/{username}")

    async def get_repositories(self, username: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Return up to ``limit`` public repositories owned by ``username``."""
        params = {"per_page": max(1, min(limit, 100)), "page": 1, "sort": "updated"}
        return await self._request(f"/users/{username}/repos", params=params)

    async def get_starred_repositories(self, username: str, limit: int = 100) -> List[str]:
        """Return repository names publicly starred by ``username``."""

        starred = await self._request(
            f"/users/{username}/starred",
            params={"per_page": max(1, min(limit, 100)), "page": 1},
        )
        return [repo.get("full_name", "") for repo in starred if repo.get("full_name")]

    async def get_events(self, username: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Return up to ``limit`` recent public events for ``username``."""

        return await self._request(
            f"/users/{username}/events/public",
            params={"per_page": max(1, min(limit, 100)), "page": 1},
        )

    async def get_full_report(self, username: str, limit: int = 100) -> Dict[str, Any]:
        """Fetch profile, repositories, and activities concurrently."""

        if not username or not username.strip():
            raise ValueError("GitHub username cannot be empty")
        if limit < 1:
            raise ValueError("limit must be at least 1")

        profile, repos, activities = await asyncio.gather(
            self.get_profile(username.strip()),
            self.get_repositories(username.strip(), limit),
            self.get_events(username.strip(), limit),
        )

        starred_names = set()
        starred_total = 0
        starred = await self.get_starred_repositories(username.strip(), limit)
        starred_names = set(starred)
        starred_total = len(starred)

        normalized_repos = [
            {
                **repo,
                "user_id": profile.get("id"),
                "has_pages": bool(repo.get("has_pages", False)),
                "starred": repo.get("full_name", "") in starred_names,
            }
            for repo in repos
        ]

        return {
            "profile": {
                "userId": profile.get("id", "N/A"),
                "login": profile.get("login", username),
                "name": profile.get("name") or "",
            },
            "repos": normalized_repos,
            "activities": activities[:10],
            "starred_total": starred_total,
        }
