# -*- coding: utf-8 -*-

"""
    wow_addon_manager.helpers
    ~~~~~~~~~~~~~~~~~~~~~

    Implements various helpers.

    :author: qwezarty
    :date: 12:43 pm Feb 4 2019
    :email: qwezarty@gmail.com
"""

from requests import Response
from pathlib import Path
from os import path
from lxml import etree

root_path = Path(__file__).parent

def cache_response(res):
    """cache last response"""
    """located at cache/last_*_response.html"""
    if not isinstance(res, Response):
        raise TypeError('cache response type only can be requests/Response')
    
    rel_path = ''
    if res.status_code == 200:
        rel_path = 'cache/last_success_response.html'
    else:
        rel_path = 'cache/last_error_response.html'

    abs_path = path.join(root_path, rel_path)
    with open(abs_path, 'w+') as f:
        f.write(res.text)

def xpath_text(html, xpath):
    import ipdb
    ipdb.set_trace()
    if not isinstance(html, str):
        raise TypeError('type could only be xx when')
    nodes = html.xpath(xpath)
    assert len(nodes) == 1, 'node selected by xpath could only be 1'
    return nodes[0].text