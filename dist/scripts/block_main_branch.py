#!/usr/bin/env python3
"""Hook: block git write-operations targeting protected branches.

Event: PreToolUse (Bash)
Exit 0 = allow, Exit 2 = block.
"""

import json
import os
import re
import sys


PROTECTED = r"(?:main|master|prod|production)"
# git checkout <branch> or git switch <branch> — but NOT checkout -b / switch -c
CHECKOUT_RE = re.compile(
    rf"git\s+(?:checkout|switch)\s+(?!-[bcB]){PROTECTED}\b"
)
# git push ... <branch>  (captures "git push origin main", "git push main")
PUSH_RE = re.compile(rf"git\s+push\b.*\b{PROTECTED}\b")
# git merge|rebase|reset ... <branch>
MERGE_RE = re.compile(rf"git\s+(?:merge|rebase|reset)\b.*\b{PROTECTED}\b")

BLOCK_PATTERNS = [CHECKOUT_RE, PUSH_RE, MERGE_RE]


def main() -> None:
    if os.environ.get("SHAKTRA_ALLOW_MAIN_BRANCH"):
        sys.exit(0)

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    command = data.get("tool_input", {}).get("command", "")
    if not isinstance(command, str) or not command.strip():
        sys.exit(0)

    for pattern in BLOCK_PATTERNS:
        if pattern.search(command):
            branch = re.search(PROTECTED, command).group()
            print(
                f"BLOCKED: Direct git operation on protected branch '{branch}'.\n"
                f"Create a feature branch instead:\n"
                f"  git checkout -b <branch-name>"
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
