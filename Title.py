# -*- coding: utf-8 -*-
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


class Title:
    def printing(self):
        init(strip=not sys.stdout.isatty())
        print ""
        cprint(figlet_format('EXTRACT', font='banner4'), 'green', attrs=['bold'])
