| File / Folder | Description |
| :--- | :--- |
| **githubinfo/** | Root directory |
| ├── `__main__.py` | Entry point for the CLI execution |
| ├── `cli.py` | Argparse configuration and layout |
| ├── `decorators.py` | Custom decorators (Auth, Cache, Timing) |
| └── **api/** | API sub-package |
| &nbsp;&nbsp;&nbsp;&nbsp;├── `__init__.py` | Package initializer |
| &nbsp;&nbsp;&nbsp;&nbsp;├── `client.py` | Async HTTP client (http/aiohttp) wrapper |
| &nbsp;&nbsp;&nbsp;&nbsp;└── `models.py` | Pydantic or TypedDict schemas for structured data |