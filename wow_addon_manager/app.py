# -*- coding: utf-8 -*-

"""
    wow_addon_manager.app
    ~~~~~~~~~~~~~~~~~~~~~

    The main application.

    :author: qwezarty
    :date: 04:03 pm Nov 14 2017
    :email: qwezarty@gmail.com
"""

import sys
import os
from .config import Config
from .request import Request

class App:
    """main application"""

    def __init__(self, import_name, root_path=None):
        self.import_name = import_name
        if root_path is None:
            root_path = self.get_root_path(import_name)
        self.root_path = root_path
        self.system_config = self.make_config('configs/system.json')
        self.user_config = self.make_config(self.system_config['user_config'])
        self.request =  self.make_request(self.user_config['source'])

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

    def make_request(self, source_name):
        """get an instance of SourceRequest, according to source_name"""
        return Request(root_path=self.root_path)
    
    def search(self, addon_name):
        """search a spesific addon."""
        addon = self.request.get_details(addon_name)
        print(addon)