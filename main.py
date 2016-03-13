#!/usr/bin/env python3

import sys
from appscript import *
from termcolor import colored, cprint
def main():
    cmd, is_open, itunes = None if len(sys.argv) == 1 else sys.argv[1], \
        app('System Events').processes[its.name == 'iTunes'].count(), \
        app('iTunes')
if __name__ == '__main__':
    main()
