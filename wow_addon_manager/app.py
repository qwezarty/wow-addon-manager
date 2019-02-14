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
from .config import Config
from .request import Request
import zipfile
from wow_addon_manager import helpers
from os import path, getcwd, mkdir, makedirs

class App:
    """main application"""

    def __init__(self, import_name, root_path=None):
        self.import_name = import_name
        if root_path is None:
            root_path = self.get_root_path(import_name)
        self.root_path = root_path
        self.system_config = self.make_config('configs/system.json', relative=True)
        self.user_config = self.make_config(self.get_user_config_path(), relative=False)
        self.addons_dir = path.join(self.user_config['wow_root_folder'], '_retail_', 'Interface', 'Addons')
        self.request =  self.make_request(self.user_config['source'])
        self.init_dirs()

    def get_root_path(self, import_name):
        """find the root path of the package"""
        mod = sys.modules.get(import_name)
        if mod is not None and hasattr(mod, '__file__'):
            return path.dirname(path.abspath(mod.__file__))
        # loader = pkgutil.get_loader(import_name)
        # if loader is None or import_name == '__main__':
        return getcwd()

    def init_dirs(self):
        """init folders if not existed."""
        cache_dir = path.join(self.root_path, 'cache')
        if not path.exists(cache_dir):
            mkdir(cache_dir)
        if self.system_config['run_mode'] == 'test':
            self.addons_dir = path.join(self.root_path, 'tests', 'dst', 'Interface', 'Addons')
        if not path.exists(self.addons_dir):
            makedirs(self.addons_dir)
    
    def get_user_config_path(self):
        """get user config file in system.json, or using default file, i.e. user.sample.json"""
        user_path = path.join(self.root_path, self.system_config['user_config'])
        default_path = path.join(self.root_path, 'configs', 'user.sample.json')
        if path.exists(user_path):
            return user_path
        print('user configed file not existed! using default config.')
        if path.exists(default_path):
            return default_path
        print('default configed file also not existed!')
        import sys
        sys.exit(1)
    
    def make_config(self, file_path, relative=False):
        """get an instance of Config, and load a json file."""
        config = Config(self.root_path)
        if relative:
            config.from_rel_json(file_path)
        else:
            config.from_abs_json(file_path)
        return config

    def make_request(self, source_name):
        """get an instance of SourceRequest, according to source_name."""
        return Request(root_path=self.root_path)
    
    def info(self, addon_id):
        """show the infomations of a specific addon."""
        addon = self.request.get_info(addon_id)
        print('name: ', addon['name'])
        print('install-id: ', addon['id'])
        print('game-version: ', addon['game_version'])
        print('last-update', addon['last_update'])
        print('addon-homepage', addon['addon_url'])

    def install(self, addon_id):
        """install a specific addon."""
        zip_file = self.request.download_to_cache(addon_id)
        print('===> Installing...', end='')
        helpers.extract_to_dst(zip_file, self.addons_dir)
        print('Done!')

    def search(self, addon_name):
        """search the addon you want."""
        addons = self.request.get_list(addon_name)
        for a in addons:
            print('%-40s%-20s' % (a['id'], a['last_update']))
