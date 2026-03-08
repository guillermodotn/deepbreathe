import argparse
import os
import re
from pathlib import Path


def get_current_version() -> str:
    """Get the current version from apno/__init__.py"""
    init_file = Path("apno/__init__.py")
    if not init_file.exists():
        return "0.1.0"

    content = init_file.read_text()
    match = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content)
    if match:
        return match.group(1)
    return "0.1.0"


def set_version(new_version: str) -> str:
    """Set the version in apno/__init__.py"""
    init_file = Path("apno/__init__.py")
    if not init_file.exists():
        init_file.parent.mkdir(exist_ok=True)
        init_file.write_text(f"__version__ = '{new_version}'\n")
    else:
        content = init_file.read_text()
        content = re.sub(
            r'__version__\s*=\s*[\'"][^\'"]*[\'"]',
            f"__version__ = '{new_version}'",
            content,
        )
        init_file.write_text(content)
    return new_version


def bump_version(bump_type: str = "patch") -> str:
    """Bump the version number based on the bump type"""
    current_version = get_current_version()
    parts = current_version.split(".")

    if len(parts) != 3:
        return "1.0.0"

    major, minor, patch = map(int, parts)

    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    else:  # patch
        patch += 1

    new_version = f"{major}.{minor}.{patch}"
    set_version(new_version)
    return new_version


def get_version_code() -> str:
    """Get the version code based on GitHub run number"""
    run_number = os.getenv("GITHUB_RUN_NUMBER", "1")
    return f"100{run_number}"


def main():
    """Command line interface for version management"""
    parser = argparse.ArgumentParser(description="Manage semantic versioning")
    parser.add_argument(
        "action", choices=["get", "set", "bump"], help="Action to perform"
    )
    parser.add_argument("value", nargs="?", help="New version or bump type")

    args = parser.parse_args()

    if args.action == "get":
        print(get_current_version())
    elif args.action == "set":
        if args.value:
            print(set_version(args.value))
        else:
            print("Error: New version required for set action")
            exit(1)
    elif args.action == "bump":
        bump_type = args.value or "patch"
        print(bump_version(bump_type))


if __name__ == "__main__":
    main()
