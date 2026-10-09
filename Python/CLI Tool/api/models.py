"""Typed structures used by the API layer."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass(frozen=True)
class Profile:
    user_id: int | str
    login: str
    name: str = ""

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> "Profile":
        return cls(data.get("id", "N/A"), data.get("login", "Unknown"), data.get("name") or "")

@dataclass(frozen=True)
class Report:
    profile: Dict[str, Any]
    repos: List[Dict[str, Any]]
    activities: List[Dict[str, Any]]

