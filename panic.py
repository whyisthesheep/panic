import argparse
import subprocess

def install(package):
    try:
        search_result = subprocess.run(["auracle", "search", "--quiet", package], capture_output=True, text=True)
        if search_result.returncode == 0 and f"^{package}$" in search_result.stdout:
            print(f"Package '{package}' found in the AUR.")
            confirm = input(f"Do you want to install '{package}' from AUR? (Y/n): ").lower()
            if confirm in {"y", ""}:
                subprocess.run(["auracle", "clone", package])
                print(f"Package '{package}' cloned successfully from AUR.")
                subprocess.run(["bash", "-c", f"cd {package} && makepkg -si"])
                print(f"Package '{package}' built and installed successfully from AUR.")
            else:
                print("Installation from AUR aborted.")
        else:
            print(f"Package '{package}' not found in the AUR.")
            confirm = input(f"Do you want to install '{package}' using pacman? (Y/n): ").lower()
            if confirm in {"y", ""}:
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
                print(f"Package '{package}' installed successfully using pacman.")
            else:
                print("Pacman installation aborted.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def search(keyword):
    try:
        auracle_search_result = subprocess.run(["auracle", "search", "--quiet", keyword], capture_output=True, text=True)
        if auracle_search_result.returncode == 0 and auracle_search_result.stdout.strip():
            print(f"Search results for keyword '{keyword}' in AUR:")
            print(auracle_search_result.stdout.strip())
        else:
            print(f"No packages found in AUR for keyword '{keyword}'.")
        pacman_search_result = subprocess.run(["pacman", "-Ss", keyword], capture_output=True, text=True)
        if pacman_search_result.returncode == 0 and pacman_search_result.stdout.strip():
            print(f"\nSearch results for keyword '{keyword}' in Pacman:")
            print(pacman_search_result.stdout.strip())
        else:
            print(f"No packages found in Pacman for keyword '{keyword}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def upgrade():
    try:
        subprocess.run(["auracle", "update"])
        print("AUR packages upgraded successfully.")
        subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
        print("Pacman packages upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="AUR wrapper tool for installing, searching, and upgrading packages")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", required=False)
    install_parser = subparsers.add_parser("install", help="Install a package from AUR")
    install_parser.add_argument("package", help="Name of the package to install")
    search_parser = subparsers.add_parser("search", help="Search for packages in AUR")
    search_parser.add_argument("keyword", help="Keyword to search for")
    upgrade_parser = subparsers.add_parser("upgrade", help="Upgrade all AUR packages")
    args = parser.parse_args()
    if args.subcommand in {"install"}:
        install(args.package)
    elif args.subcommand in {"search"}:
        search(args.keyword)
    elif args.subcommand in {"upgrade"} or not args.subcommand:
        upgrade()

if __name__ == "__main__":
    main()
