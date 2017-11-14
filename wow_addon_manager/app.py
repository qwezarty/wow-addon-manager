# -*- coding: utf-8 -*-

"""
    app.py
    ~~~~~~~~~~~~~~~~~~~~~

    The main application.

    :author: qwezarty
    :date: 04:03 pm Nov 14 2017
    :email: qwezarty@gmail.com
"""

import sys
import os
from .config import Config

class App:
    """main application"""

    config_class = Config

    def __init__(self, import_name, root_path=None):
        self.import_name = import_name
        if root_path is None:
            root_path = self.get_root_path(import_name)
        self.root_path = root_path
        self.config = self.make_config()

    def get_root_path(self, import_name):
        """find the root path of the package"""
        mod = sys.modules.get(import_name)
        if mod is not None and hasattr(mod, '__file__'):
            return os.path.dirname(os.path.abspath(mod.__file__))
        # loader = pkgutil.get_loader(import_name)
        # if loader is None or import_name == '__main__':
        return os.getcwd()

    def make_config(self):
        """initial config"""
        return self.config_class(self.root_path)
