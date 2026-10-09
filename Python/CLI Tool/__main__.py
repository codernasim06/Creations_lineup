"""Executable entry point."""
from __future__ import annotations
import asyncio, sys
from api.client import GitHubAPIError, GitHubAsyncClient
from cli import parse_args, process_metrics, render_output

async def async_main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise ValueError("--limit must be at least 1")
    client = GitHubAsyncClient(token=args.token)
    try:
        print(f"Fetching metrics from '{args.user}'...")
        raw_data = await client.get_full_report(args.user, limit=args.limit)
        metrics, activities = process_metrics(raw_data)
        render_output(metrics, activities)
    finally:
        await client.close()

def main() -> None:
    try:
        asyncio.run(async_main())
    except (GitHubAPIError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    except KeyboardInterrupt:
        print("Operation canceled.")
        raise SystemExit(130)

if __name__ == "__main__":
    main()

