# Panic
The scariest AUR Helper.

## Details
Panic is a simple AUR/pacman wrapper made with python. This is not supposed to be a replacement for anything it's more of a proof of concept for a fully featured AUR helper I might make.

## Installation

1. Clone the repo `git clone https://github.com/whyisthesheep/panic.git`
2. Install panic with `cd panic && makepkg -si`

## Usage
```
usage: panic [-h] {install,check,upgrade,remove}
Running panic by itself will upgrade

AUR wrapper tool for installing, searching, and upgrading packages

options:
  -h, --help            show this help message and exit

subcommands:
    install             Install a package from AUR
    check               Search for packages in AUR
    upgrade             Upgrade all AUR packages
    remove              Remove a package
```
