# -*- coding: utf-8 -*-

"""
    wow_addon_manager.request
    ~~~~~~~~~~~~~~~~~~~~~

    Implements the basic request to web.
    A component that can make request to source(e.g. curse/wowinterface)

    :author: qwezarty
    :date: 6:55 pm Apr 1 2018
    :email: qwezarty@gmail.com
"""

from wow_addon_manager.sources.curseforge import Curseforge
from wow_addon_manager.sources.wowinterface import Wowinterface
import requests
from os import path
from wow_addon_manager import helpers

class Request:
    def __init__(self, root_path, source_name='curseforge'):
        self.root_path = root_path
        self.source_name = ''
        self.source = self._get_source(source_name)
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'}

    def _get_source(self, source_name):
        """init the source class"""
        if source_name == 'curseforge':
            self.source_name = source_name
            return Curseforge()
        elif source_name == 'wowinterface':
            self.source_name = source_name
            return Wowinterface()
        else:
            raise ValueError('source name is invalid.')

    def change_source(self, source_name):
        """change request source, 
        curseforge and wowinterface is supported for now."""
        self.source = self._get_source(source_name)
    
    def get_list(self, addon_name):
        """get a list of addon you search via addon name"""
        print('===> Searching %s from %s...' %(addon_name, self.source_name), end='')
        url = self.source.get_search_url(addon_name)
        params = self.source.get_search_qs(addon_name)
        res = requests.get(url=url, headers=self.headers, params=params)
        helpers.cache_response(res)
        print('Done!')
        return self.source.analyze_search(res)
    
    def get_info(self, addon_id):
        """get an specific addon's detail via addon id"""
        print('===> Collecting metadata of %s...' % addon_id, end='')
        url = self.source.get_info_url(addon_id)
        params = self.source.get_info_qs(addon_id)
        res = requests.get(url=url, headers=self.headers, params=params)
        helpers.cache_response(res)
        print('Done!')
        return self.source.analyze_info(res)

    def download_to_cache(self, addon_id):
        """download addon to cache and return absolute path of zip file."""
        addon = self.get_info(addon_id)
        s = requests.session()
        print('===> Collecting download url of %s...' % addon_id, end='')
        res = s.get(addon['download_url'])
        print('Done!')
        abs_path = path.join(self.root_path, 'cache', addon['name'] + '.zip')
        print('===> Downloading addon: %s...' % addon_id, end='')
        with open(abs_path, 'wb+') as f:
            f.write(res.content)
        s.close()
        print('Done!')
        return abs_path

