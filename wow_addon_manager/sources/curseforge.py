# -*- coding: utf-8 -*-

"""
    wow_addon_manager.sources.curseforge
    ~~~~~~~~~~~~~~~~~~~~~

    Xpath rules and request to curseforge.

    :author: qwezarty
    :date: 05:08 pm Jan 22 2019
    :email: qwezarty@gmail.com
"""

from lxml import etree
from wow_addon_manager import helpers
import requests

class Curseforge():
    def __init__(self):
        self.home_url = 'https://www.curseforge.com'
        self.base_url = 'https://www.curseforge.com/wow/addons'

    def analyze_details(self, res):
        """analyze response and return a standard addon entity"""
        html = etree.HTML(res.text)
        addon_id = self._handle_id(res.url)
        name = helpers.xpath_text(html, '//meta[@property="og:title"]', 'content')
        desc = helpers.xpath_text(html, '//meta[@property="og:description"]', 'content')
        raw_game_version = helpers.xpath_text(html, '//header//span[@class="stats--game-version"]')
        game_version = self._handle_game_version(raw_game_version)
        last_update = helpers.xpath_text(html, '//header//span[@class="stats--last-updated"]/abbr')
        image = helpers.xpath_text(html, '//meta[@property="og:image"]', 'content')
        download_url = self._get_real_download_url(res.url)

        return {
            'id': addon_id,
            'name': name,
            'game_version': game_version,
            'last_update': last_update,
            'description': desc,
            'image': image,
            'addon_url': res.url,
            'download_url': download_url
        }

    def _handle_game_version(self, game_version):
        """change Game Version: 8.1.0 --> '8.1.0"""
        l = game_version.split(' ')
        return l[len(l)-1]

    def _handle_id(self, addon_url):
        """get addon_id from addon_url"""
        l = addon_url.split('/')
        return l[len(l)-1]

    def _get_real_download_url(self, addon_url):
        download_page_url = '/'.join([addon_url, 'download'])
        res = requests.get(download_page_url)
        helpers.cache_response(res, 'download_page.html')

        html = etree.HTML(res.text)
        rel_url = helpers.xpath_text(html, '//main//a[@class="download__link"]', 'href')
        download_url = ''.join([self.home_url, rel_url])

        return download_url