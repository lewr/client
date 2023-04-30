#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import helpers
import servers

def main():
    try:
        while True:
            name = input("имя: ").strip()
            fix_name = helpers.fix_name(name)
            if name:              
                servers.find(name, fix_name)    

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()