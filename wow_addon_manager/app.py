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

    def __init__(self, import_name, root_path=None):
        self.import_name = import_name
        if root_path is None:
            root_path = self.get_root_path(import_name)
        self.root_path = root_path
        self.system_config = self.make_config("configs/system.json")
        self.user_config = self.make_config(self.system_config["user_config"])

    def get_root_path(self, import_name):
        """find the root path of the package"""
        mod = sys.modules.get(import_name)
        if mod is not None and hasattr(mod, '__file__'):
            return os.path.dirname(os.path.abspath(mod.__file__))
        # loader = pkgutil.get_loader(import_name)
        # if loader is None or import_name == '__main__':
        return os.getcwd()
    
    def make_config(self, file_name):
        """get an instance of Config, and load a json file"""
        config = Config(self.root_path)
        config.from_json(file_name)
        return config
