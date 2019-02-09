# -*- coding: utf-8 -*-

import pytest
from requests import Response
from os import path, remove
import os
from pathlib import Path
from wow_addon_manager import helpers

root_path = Path(__file__).parent.parent

def test_cache_success_response():
    res = Response()
    res.status_code = 200
    helpers.cache_response(res, 'test_cache.html')
    abs_path = path.join(root_path, 'cache', 'success_test_cache.html')
    assert path.exists(abs_path)
    remove(abs_path)
    
def test_cache_error_response():
    res = Response()
    res.status_code = 500
    helpers.cache_response(res, 'test_cache.html')
    abs_path = path.join(root_path, 'cache', 'error_test_cache.html')
    assert path.exists(abs_path)
    remove(abs_path)
