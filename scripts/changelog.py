import argparse
import re
import subprocess
import sys


def parse_commits(commits: list[str]) -> dict[str, list[str]]:
    """Parse commit messages and categorize them by type"""
    categories = {
        "Features": [],
        "Bug Fixes": [],
        "Documentation": [],
        "Performance": [],
        "Breaking Changes": [],
    }

    for commit in commits:
        commit = commit.strip()
        if not commit:
            continue

        match = re.match(
            r"(feat|fix|docs|style|refactor|test|chore|perf|ci)(?:\(([^)]+)\))?:\s*(.*)",
            commit,
        )
        if match:
            type_, scope, description = match.groups()
            scope_str = f"({scope}) " if scope else ""

            if type_ == "feat":
                categories["Features"].append(f"{scope_str}{description}")
            elif type_ == "fix":
                categories["Bug Fixes"].append(f"{scope_str}{description}")
            elif type_ == "docs":
                categories["Documentation"].append(f"{scope_str}{description}")
            elif type_ == "perf":
                categories["Performance"].append(f"{scope_str}{description}")
            elif type_ == "refactor":
                categories["Performance"].append(f"Refactor: {description}")
            elif type_ == "test":
                categories["Documentation"].append(f"Test: {description}")
            elif type_ == "chore":
                categories["Documentation"].append(f"Chore: {description}")
            elif type_ == "ci":
                categories["Documentation"].append(f"CI: {description}")

            if "BREAKING CHANGE" in commit.upper():
                categories["Breaking Changes"].append(f"{scope_str}{description}")
        else:
            categories["Features"].append(commit)

    return categories


def generate_release_notes(categories: dict[str, list[str]]) -> str:
    """Generate release notes from categorized commits"""
    notes = []

    for category, items in categories.items():
        if items:
            notes.append(f"## {category}")
            for item in items:
                notes.append(f"- {item}")
            notes.append("")

    return "\n".join(notes).strip()


def get_commits_since_tag(tag: str) -> list[str]:
    """Get commit messages since a specific tag"""
    try:
        result = subprocess.run(
            ["git", "log", f"{tag}..HEAD", "--pretty=format:%s"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        return []


def get_all_commits(limit: int = 50) -> list[str]:
    """Get recent commit messages"""
    try:
        result = subprocess.run(
            ["git", "log", f"-{limit}", "--pretty=format:%s"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        return []


def main():
    """Command line interface for changelog generation"""
    parser = argparse.ArgumentParser(description="Generate release notes from commits")
    parser.add_argument(
        "action",
        choices=["parse", "generate", "get-commits"],
        help="Action to perform",
    )
    parser.add_argument(
        "--since",
        help="Get commits since this tag",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Number of commits to get (default: 50)",
    )

    args = parser.parse_args()

    if args.action == "get-commits":
        if args.since:
            commits = get_commits_since_tag(args.since)
        else:
            commits = get_all_commits(args.limit)
        for commit in commits:
            print(commit)
    elif args.action == "parse":
        commits = [line for line in sys.stdin.read().strip().split("\n") if line]
        categories = parse_commits(commits)
        print(generate_release_notes(categories))
    elif args.action == "generate":
        if args.since:
            commits = get_commits_since_tag(args.since)
        else:
            commits = get_all_commits(args.limit)
        categories = parse_commits(commits)
        print(generate_release_notes(categories))


if __name__ == "__main__":
    main()
