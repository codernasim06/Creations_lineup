"""Text formatting helpers."""
from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List

def render_report(metrics: Dict[str, Any], activities: List[Dict[str, Any]]) -> str:
    name = metrics.get("name") or ""
    identity = metrics.get("login", "Unknown") + (f" ({name})" if name else "")
    rule = "=" * max(50, len(identity) + 24)
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = [rule, f"GitHub public profile: {identity}", f"User ID: {metrics.get('user_id', 'N/A')}",
             f"As of: {timestamp}", rule,
             f"Public repositories: {metrics.get('repo_count', 0)} total",
             rule, f"Recent public activities: {len(activities)} events"]
    if not activities:
        lines.append("No recent event histories found")
    else:
        for index, event in enumerate(activities, 1):
            event_type = str(event.get("type", "GenericEvent")).replace("Event", "")
            repo_name = (event.get("repo") or {}).get("name", "Unknown/Repository")
            lines.append(f" {index:02d}. [{str(event.get('created_at', ''))[:10] or 'unknown date'}] -> {event_type:<15} @ {repo_name}")
    lines.append(rule)
    return "\n".join(lines)
