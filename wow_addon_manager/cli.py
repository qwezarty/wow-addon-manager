# -*- coding: utf-8 -*-

"""
    wow_addon_manager.cli
    ~~~~~~~~~~~~~~~~~~~~~

    A simple command line application to run wow-addon-manager apps.

    :author: qwezarty
    :date: 07:35 pm Jan 08 2019
    :email: qwezarty@gmail.com
"""

import sys
import argparse
from wow_addon_manager import install
from wow_addon_manager import search

def _parse_args():
    parser = argparse.ArgumentParser()

    _init_general_parsers(parser)
    _init_subparsers(parser)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()

def _init_general_parsers(parser):
    parser.add_argument(
        '-v', '--version',
        action = 'version',
        version = '%(prog)s 0.0.1',
        help = 'show version and exit.'
    )

def _init_subparsers(parent):
    subparsers = parent.add_subparsers()

    parser_install = subparsers.add_parser(
        'install',
        help = 'install a specific addon.'
    )
    install.init_parser(parser_install)
    parser_install.set_defaults(func=install.main)
    parser_install.add_argument(
        "addon",
        help = "the addon you want to install"
    )

    parser_search = subparsers.add_parser(
        'search',
        help = 'search for addons.'
    )
    search.init_parser(parser_search)
    parser_search.set_defaults(func=search.main)
    parser_search.add_argument(
        "addon",
        help = "the addon you want to search"
    )

def main():
    # print('welcome to use wow-addon-manager cli tool!')
    # if args is None:
    #     print("you should add a sub-command")
    
    args = _parse_args()
    if hasattr(args, 'func'):
        args.func(args)