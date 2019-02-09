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

class Curseforge():
    def __init__(self):
        self.base_url = 'https://www.curseforge.com/wow/addons'

    def analyze_details(self, res):
        """analyze response and return a standard addon entity"""
        html = etree.HTML(res.text)
        name = helpers.xpath_text(html, '//header//h2[@*="name"]')
        raw_game_version = helpers.xpath_text(html, '//header//span[@class="stats--game-version"]')
        game_version = self._handle_game_version(raw_game_version)
        last_update = helpers.xpath_text(html, '//header//span[@class="stats--last-updated"]/abbr')
        return {
            'name': name,
            'game_version': game_version,
            'last_update': last_update,
            'url': res.url
        }

    def _handle_game_version(self, game_version):
        """change Game Version: 8.1.0 --> '8.1.0"""
        l = game_version.split(' ')
        return l[len(l)-1]
