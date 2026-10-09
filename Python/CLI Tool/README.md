# GitHub Public Activity CLI

A lightweight Python command-line tool for inspecting a GitHub user’s public profile, public repository count, and latest public activity history.

The tool is designed to be simple to run, easy to understand, and straightforward to extend.

## What it does

Given a GitHub username, the CLI:

1. Requests the user’s public profile from GitHub.
2. Retrieves the user’s public repositories.
3. Retrieves the user’s public events.
4. Processes the API response into a small report.
5. Prints the total public repository count and the latest 10 public activities.

The report includes a local timestamp so the result clearly shows when it was generated.

## Project workflow

```text
Command-line arguments
        |
        v
GitHubAsyncClient
  |       |       |
  v       v       v
Profile  Repos   Events
        |
        v
process_metrics()
        |
        v
render_report()
        |
        v
Formatted terminal output
```

## Project structure

| File | Responsibility |
| --- | --- |
| `__main__.py` | Application entry point. Starts the async event loop, coordinates the client, and handles user-facing errors. |
| `cli.py` | Defines command-line arguments, transforms raw API data into metrics, and sends the report to the formatter. |
| `api/client.py` | Implements the asynchronous GitHub REST API client using Python’s standard library. Handles requests, timeouts, JSON responses, and API errors. |
| `api/models.py` | Contains lightweight dataclasses representing profile and report structures. |
| `api/__init__.py` | Marks the API directory as a Python package. |
| `utils/formatter.py` | Converts processed metrics and events into readable terminal output. |
| `decorators.py` | Provides reusable async timing and API-error decorator utilities. |
| `Architecture.md` | Short architecture reference for the project. |

## Requirements

- Python 3.10 or newer
- Internet access to `api.github.com`

The API client uses only Python’s standard library, so no third-party package installation is required.

## Run the tool

From this directory, run:

```powershell
python __main__.py --user codernasim06
```

You can also choose how many repositories to request from GitHub. The activity output remains limited to the latest 10 public activities:

```powershell
python __main__.py --user octocat --limit 50
```

Display command help with:

```powershell
python __main__.py --help
```

## Example output

```text
==================================================
GitHub public profile: codernasim06
User ID: 123456789
As of: 2026-10-09 20:44:10 Bangladesh Standard Time
==================================================
Public repositories: 12 total
==================================================
Recent public activities: 10 events
 01. [2026-10-09] -> Push            @ codernasim06/project
 02. [2026-10-08] -> Create          @ codernasim06/another-project
==================================================
```

## Public data and authentication

Repository and activity collection intentionally uses GitHub’s public endpoints. A token is not required for public information.

GitHub may rate-limit unauthenticated requests. The client accepts an optional token for API authentication, but the report remains public-only and does not include private repositories.

## Error handling

The client converts network failures, timeouts, invalid JSON, and GitHub HTTP errors into `GitHubAPIError`. The entry point catches these errors and displays a concise message before exiting with a failure status.

Typical causes include:

- Misspelled or nonexistent usernames
- No internet connection
- GitHub API rate limiting
- Temporary GitHub service errors

## Development checks

Compile the complete project:

```powershell
python -m compileall -q .
```

Run the CLI help smoke test:

```powershell
python __main__.py --help
```

## Design notes

- Network calls are asynchronous and run concurrently where possible.
- The standard library keeps installation minimal.
- API access, data processing, and presentation are separated into different modules.
- The formatter is independent of the HTTP client, making output changes safe and easy.
