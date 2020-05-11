import os
import textwrap
import json
import re
import difflib
import click
import colorama

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--no-colour", "-nc", is_flag=True, help="Disable colours.")
@click.option("--heat-map", "-hm", is_flag=True, help="Heat map based on file size.")
@click.option("--no-ansi", "-na", is_flag=True, help="Make colours work on non-ansi supported terminals, but not underlines.")
def bls(no_colour, heat_map, no_ansi):
    if no_ansi:
        colorama.init()

    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "filenames.json")
    ) as file:
        filesnames = json.load(file)

    files = []
    replacelist = []
    with os.scandir(".") as it:
        for entry in it:
            name = entry.name
            if not no_colour:
                if heat_map:
                    if entry.is_dir():
                        name = "\033[1;36m\033[4m" + name + "\033[0m"
                    elif entry.stat().st_size > 1000000000: # 1 gigabyte
                        name = "\033[0;31m" + name + "\033[0m"
                    elif entry.stat().st_size > 1000000: # 1 megabyte
                        name = "\033[1;31m" + name + "\033[0m"
                    elif entry.stat().st_size > 1000: # 1 kilobyte
                        name = "\033[1;33m" + name + "\033[0m"
                else:
                    if entry.is_dir():
                        name = "\033[92m\033[4m" + name + "\033[0m"
                    elif name.lower().startswith("readme") or name in filesnames["immediate"]:
                        name = "\033[1;33m" + name + "\033[0m"
                    elif name.endswith(tuple(filesnames["image"])):
                        name = "\033[0;35m" + name + "\033[0m"
                    elif name.endswith(tuple(filesnames["video"])):
                        name = "\033[0;36m" + name + "\033[0m"
                    elif name.endswith(tuple(filesnames["music"])):
                        name = "\033[0;34m" + name + "\033[0m"
                    elif name.endswith(tuple(filesnames["document"])):
                        name = "\033[1;34m" + name + "\033[0m"
                    elif name.endswith(tuple(filesnames["compressed"])):
                        name = "\033[1;35m\033[4m" + name + "\033[0m"
                replacelist.append([entry.name, name])
            else:
                if entry.is_dir():
                    replacelist.append([entry.name, "\033[4m" + name + "\033[0m"])
            files.append(entry.name)

    width = os.get_terminal_size().columns
    text = "\n".join(
        textwrap.wrap(
            "\t".join(files),
            width=width,
            break_on_hyphens=False,
            break_long_words=False,
            tabsize=23,
        )
    )
    position = 0
    for pair in replacelist:
        newtext = text[:position] + re.sub(r"(?i)(?<!\S)" + re.escape(pair[0]) + r"\b", lambda x: pair[1], text[position:], 1)
        diff = difflib.ndiff(text, newtext)
        for pos, d in enumerate(diff):
            if d[0] == "+":
                position = pos
        text = newtext

    print(text)

if __name__ == "__main__":
    bls()
