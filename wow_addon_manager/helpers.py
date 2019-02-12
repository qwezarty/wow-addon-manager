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
from os import path, mkdir, listdir, remove
from shutil import copytree, copy2, rmtree
import base64
from lxml import etree
import zipfile

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

def xpath_text(html, xpath, attr=''):
    """use xpath to get element's attribute from html"""
    """by default, it gets the text of node"""
    nodes = html.xpath(xpath)
    assert len(nodes) == 1, 'node selected by xpath could only be 1'
    node = nodes[0]
    if attr == '':
        return node.text
    else:
        return node.get(attr)

def extract_to_dst(src, dst):
    """extract addon src zip file to destination."""
    copied_items = []
    zip_file = path.basename(src)
    zip_name, _ = path.splitext(zip_file)
    cache_path = path.join(root_path, 'cache', zip_name)
    with zipfile.ZipFile(src, 'r') as z:
        # create folder and extract to cache
        mkdir(cache_path)
        z.extractall(cache_path)
        trim_os_hidden_files(cache_path)

        top_levels = [path.join(cache_path, c) for c in listdir(cache_path)]
        if len(top_levels) > 1:
            # zip's top-level has multiple files or folder
            # if it contains only folders, we should copy everything to dst
            # otherwize, this is not a standard addon package, we should raise an exception
            if not only_dirs_or_not(cache_path):
                remove_src(cache_path)
                raise Exception('addon-zip contents contain file, this is not a standard addon.')
            results = copy_contents(cache_path, dst)
            copied_items.extend(results)
        elif len(top_levels) == 1:
            if not only_dirs_or_not(top_levels[0]):
                # extracted-folder which contains files and folders.
                # it means that we only should copy this folder to dst
                result = copy_src_to_dst(top_levels[0], dst)
                copied_items.append(result)
            else:
                # extracted-folder which contains only folders. 
                # it means that we should copy every sub-folders to dst
                results = copy_contents(top_levels[0], dst)
                copied_items.extend(results)
    # delete cache folder before return
    remove_src(cache_path)
    return copied_items

def trim_os_hidden_files(abs_path):
    """trim os hidden files and folder like: .DS_Store, """
    pass

def only_dirs_or_not(abs_path):
    """check abs_path's contents."""
    """return True if they are all folders, or False if any file."""
    contents = listdir(abs_path)
    for c in contents:
        abs_c = path.join(abs_path, c)
        if not path.isdir(abs_c):
            return False
    return True

def copy_contents(src, dst):
    """copy every src's contents to dst."""
    """if dst is already existed, remove it before copy."""
    copied_items = []
    contents = listdir(src)
    for c in contents:
        abs_c = path.join(src, c)
        abs_dst = copy_src_to_dst(abs_c, dst)
        copied_items.append(abs_dst)
    return copied_items

def copy_src_to_dst(src, dst_dir):
    """copy src to dst. works for both file and dir."""
    """if dst is already existed, remove it first then copy."""
    abs_dst = path.join(dst_dir, path.basename(src))
    if path.isdir(src):
        if path.exists(abs_dst):
            rmtree(abs_dst)
        copytree(src, abs_dst)
    else:
        if path.exists(abs_dst):
            remove(abs_dst)            
        copy2(src, abs_dst)
    return abs_dst

def remove_src(src):
    """recursively remove if src is a folder, or remove if src is a file."""
    if path.isdir(src):
        rmtree(src)
    else:
        remove(src)
