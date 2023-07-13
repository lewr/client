#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import helpers
import servers


def main():
    try:
        while True:
            names = get_names()
            if all(names):
                servers.search(names)

    except KeyboardInterrupt:
        pass


def get_names():
    """entering a name from the keyboard and getting
    options from the transliteration or correcting the layout
    name   -> fix_name, for example:
    ghbdtn -> привет
    привет -> privet
    privet -> привет
    """
    name = input("имя: ").strip()
    fix_name = helpers.fix_name(name)
    return [name, fix_name]


if __name__ == "__main__":
    main()
