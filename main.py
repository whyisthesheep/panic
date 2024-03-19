import argparse
import subprocess

import argparse
import subprocess

def install(package):
    try:
        search_result = subprocess.run(["auracle", "search", "--quiet", package], capture_output=True, text=True)
        if search_result.returncode != 0:
            print(f"Package '{package}' does not exist in the AUR.")
            return
        print(f"Package '{package}' found in the AUR.")
        confirm = input(f"Do you want to install '{package}'? (Y/n): ").lower()
        if confirm not in {"y", "Y", ""}:
            print("Installation aborted.")
            return
        subprocess.run(["auracle", "clone", package])
        print(f"Package '{package}' cloned successfully from AUR.")
        subprocess.run(["bash", "-c", f"cd {package} && makepkg -si"])
        print(f"Package '{package}' built and installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def search(keyword):
    print(f"Searching AUR for packages related to '{keyword}'...")

def upgrade():
    print("Upgrading all AUR packages...")

def main():
    parser = argparse.ArgumentParser(description="AUR wrapper tool for installing, searching, and upgrading packages")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", required=True)

    install_parser = subparsers.add_parser("install", aliases=["I"], help="Install a package from AUR")
    install_parser.add_argument("package", help="Name of the package to install")

    search_parser = subparsers.add_parser("search", aliases=["S"], help="Search for packages in AUR")
    search_parser.add_argument("keyword", help="Keyword to search for")

    upgrade_parser = subparsers.add_parser("upgrade", aliases=["U"], help="Upgrade all AUR packages")

    args = parser.parse_args()

    if args.subcommand in {"install", "I"}:
        install(args.package)
    elif args.subcommand in {"search", "S"}:
        search(args.keyword)
    elif args.subcommand in {"upgrade", "U"}:
        upgrade()

if __name__ == "__main__":
    main()
