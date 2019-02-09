# -*- coding: utf-8 -*-

"""
    wow_addon_manager.helpers
    ~~~~~~~~~~~~~~~~~~~~~

    Implements various helpers.

    :author: qwezarty
    :date: 12:43 pm Feb 4 2019
    :email: qwezarty@gmail.com
"""

import requests
from pathlib import Path
from os import path
import base64
from lxml import etree

root_path = Path(__file__).parent

def cache_response(res, name='last_response.html'):
    """cache last response"""
    """located at cache/last_*_response.html"""
    if not isinstance(res, requests.Response):
        raise TypeError('cache response type only can be requests/Response')
    
    file_name = ''
    if res.status_code == 200:
        file_name = ''.join(['success_', name])
    else:
        file_name = ''.join(['error_', name])

    abs_path = path.join(root_path, 'cache', file_name)
    with open(abs_path, 'w+') as f:
        f.write(res.text)

def get_and_cache(url, params=None, **kwargs):
    """get from cache if last response is success and less than 10 min"""
    """or get and cache response"""
    file_name = base64.encodestring(url.encode('utf-8')).decode('utf-8') + '.html'
    abs_success_path = path.join(root_path, 'cache', 'success_' + file_name)
    if path.exists(abs_success_path):
        res = requests.Response()
        res.status_code = 200
        res.url = url
        with open(abs_success_path, 'r') as f:
            res.text = f.read()
        return res
    res = requests.get(url, params, **kwargs)
    cache_response(res, file_name)
    return res

def xpath_text(html, xpath):
    nodes = html.xpath(xpath)
    assert len(nodes) == 1, 'node selected by xpath could only be 1'
    return nodes[0].text