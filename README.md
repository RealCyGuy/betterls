# BetterLS [![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FRealCyGuy%2Fbetterls)](https://twitter.com/intent/tweet?text=This%20is%20hands%20down%20the%20BEST%20GitHub%20repo%20in%20the%20entirety%20of%20GitHub.%20Just%20very%2C%20very%2C%20very%2C%20very%2C%20very%2C%20very%20amazing.%20You%20should%20definitely%20check%20them%20out:&url=https%3A%2F%2Fgithub.com%2FRealCyGuy%2Fbetterls)

*A better ls command than windows `dir`. Not sure about linux though. :|*

[![Version](https://img.shields.io/pypi/v/betterls?label=latest%20version&style=for-the-badge)](https://github.com/RealCyGuy/betterls/releases/latest)
[![PyPI - Downloads](https://img.shields.io/pypi/dd/betterls?style=for-the-badge)](https://pypi.org/project/betterls)
[![GitHub license](https://img.shields.io/github/license/realcyguy/betterls?style=for-the-badge)](https://github.com/RealCyGuy/betterls/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/realcyguy/betterls?style=for-the-badge)](https://github.com/realcyguy/betterls/issues)

Look how cool:
![bls](https://i.imgur.com/5EzMyjX.png)

## Installation

Use [PIP](https://pypi.org/project/betterls/):

```bash
pip install --upgrade betterls
```

## Usage

If you're on Windows, use a ANSI escape code compatible terminal (like Windows Terminal) or use `--no-ansi`/`-na`.

```
Usage: bls [OPTIONS]

Options:
  -nc, --no-colour  Disable colours.
  -hm, --heat-map   Heat map based on file size.
  -na, --no-ansi    Make colours work on non-ansi supported terminals, but not
                    underlines.

  -h, --help        Show this message and exit.
```

## Features

- Auto-columns.
- Highlight for different file types.
- List out files.
- Heat map.
- A help command.
- Support for non-ansi terminals.

## Changelog

https://github.com/RealCyGuy/betterls/releases/

## License

[MIT](https://github.com/RealCyGuy/betterls/blob/master/LICENSE) license.
