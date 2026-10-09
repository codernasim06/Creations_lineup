"""Command-line interface for the GitHub information client."""
from __future__ import annotations
import argparse, os
from typing import Any, Dict, List, Tuple
from utils.formatter import render_report

def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="githubinfo", description="Monitor GitHub profile metrics, repositories, and recent events.")
    parser.add_argument("-u", "--user", required=True, help="Target GitHub username")
    parser.add_argument("-l", "--limit", type=int, default=30, help="Maximum number of repositories and events to retrieve (default: 30)")
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"), help="GitHub token (or set GITHUB_TOKEN)")
    return parser.parse_args(argv)

def process_metrics(raw_data: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    profile, repos, activities = raw_data.get("profile") or {}, raw_data.get("repos") or [], raw_data.get("activities") or []
    metrics = {"user_id": profile.get("userId", "N/A"), "login": profile.get("login", "Unknown"),
               "name": profile.get("name", ""), "repo_count": len(repos)}
    return metrics, activities

def render_output(metrics: Dict[str, Any], activities: List[Dict[str, Any]]) -> None:
    print(render_report(metrics, activities))
