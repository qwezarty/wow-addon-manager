# -*- coding: utf-8 -*-

"""
    wow_addon_manager.__main__
    ~~~~~~~~~~~~~~~~~~~~~

    Alias for wow-addon-manager for command line.

    :author: qwezarty
    :date: 04:29 pm Jan 09 2019
    :email: qwezarty@gmail.com
"""

import os.path
import sys

if __package__ == '':
    # __file__ is pip-*.whl/pip/__main__.py
    # __file__ is wow-addon-manager-*/wow-addon-manager/__main__.py
    # first dirname call strips of '/__main__.py', second strips off '/wow-addon-manager'
    # Resulting path is the name of the wheel itself
    # Add that to sys.path so we can import wow-addon-manager
    # this code snippet is excerpted from github.com/pypa/pip
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from wow_addon_manager.cli import main as cli_main

if __name__ == "__main__":
    cli_main()