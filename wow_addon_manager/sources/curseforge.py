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
        # name = html.xpath('//header//h2[@*="name"]')[0].text
        name = helpers.xpath_text(html, '//header//h2[@*="name"]')
        # game_version = html.xpath('//header')
        # last_update = html.xpath('//header//span[@class="stats--last-updated"]/abbr')[0].text
        print(name)
        return True
