# -*- coding: utf-8 -*-

import pytest
from requests import Response
from os import path, remove, mkdir
from pathlib import Path
from wow_addon_manager import helpers
from shutil import rmtree

root_path = Path(__file__).parent.parent
cache_path = path.join(root_path, 'cache')
addon_src = path.join(root_path, 'tests', 'src')
addon_dst = path.join(root_path, 'tests', 'dst')

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

def test_only_dirs_or_not():
    only_dirs = path.join(root_path, 'tests', 'only_dirs')
    only_dirs_main = path.join(only_dirs, 'main')
    only_dirs_sub = path.join(only_dirs, 'sub')
    mkdir(only_dirs)
    mkdir(only_dirs_main)
    mkdir(only_dirs_sub)
    assert helpers.only_dirs_or_not(only_dirs), 'only dirs should return True.'
    rmtree(only_dirs)
    dir_and_file = path.join(root_path, 'tests', 'dir_and_file')
    dir_and_file_folder = path.join(dir_and_file, 'folder')
    dir_and_file_rdme = path.join(dir_and_file, 'readme')
    mkdir(dir_and_file)
    mkdir(dir_and_file_folder)
    with open(dir_and_file_rdme, 'w+', encoding='utf-8') as f:
        f.write('readme')
    assert not helpers.only_dirs_or_not(dir_and_file), 'only dirs should return False.'
    rmtree(dir_and_file)

def test_copy_contents():
    """test copy contents if dst is already existed."""
    # create addon src
    addon_path = path.join(root_path, 'tests', 'src', 'addon')
    addon_main = path.join(root_path, 'tests', 'src', 'addon', 'addon_main')
    addon_sub = path.join(root_path, 'tests', 'src', 'addon', 'addon_sub')
    addon_rdme = path.join(root_path, 'tests', 'src', 'addon', 'readme')
    addon_toc = path.join(root_path, 'tests', 'src', 'addon', 'addon_main', 'addon_main.toc')
    mkdir(addon_path)
    mkdir(addon_main)
    mkdir(addon_sub)
    with open(addon_rdme, 'w+', encoding='utf-8') as f:
        f.write('readme')
    with open(addon_toc, 'w+', encoding='utf-8') as f:
        f.write('addon_main.toc')
    # create addon_main which already existed inside dst
    dst = path.join(root_path, 'tests', 'dst', 'addon')
    dst_main = path.join(root_path, 'tests', 'dst', 'addon', 'addon_main')
    mkdir(dst)
    mkdir(dst_main)

    # copy contents to dst
    copied_items = helpers.copy_contents(addon_path, dst)

    # assertions
    dst_sub = path.join(root_path, 'tests', 'dst', 'addon', 'addon_sub')
    dst_main_toc = path.join(root_path, 'tests', 'dst', 'addon', 'addon_main', 'addon_main.toc')
    dst_rdme = path.join(root_path, 'tests', 'dst', 'addon', 'readme')
    assert len(copied_items) == 3
    assert path.exists(dst_sub)
    assert path.exists(dst_main_toc), 'addon_main should be override after copy contents.'
    assert path.exists(dst_rdme), 'copy contents should also work for single file.'

    # remove everything created
    rmtree(addon_path)
    rmtree(dst)

def test_extract_addon_type_one():
    """addon contains only one top-level， no nested folder outside"""
    zip_file = path.join(addon_src, 'addon_type_one.zip')
    copied_items = helpers.extract_to_dst(zip_file, addon_dst)
    assert len(copied_items) == 1, 'addon-type-one only contains one folder.'
    addon_main = path.join(addon_dst, 'addon_main')
    basename = path.basename(copied_items[0])
    assert basename == 'addon_main', "addon-type-one's folder name should be addon_main."
    addon_main_toc = path.join(addon_main, 'main.toc')
    addon_main_xml = path.join(addon_main, 'main.xml')
    assert path.exists(addon_main_toc), 'folder contents should be copied after extract to dst.'
    assert path.exists(addon_main_xml), 'folder contents should be copied after extract to dst.'

    # remove everything created
    rmtree(addon_main)
    cache_folder = path.join(cache_path, 'addon_type_one')
    assert not path.exists(cache_folder), 'cache should be remove after addon-type-one installed.'
    assert not path.exists(addon_main)

def test_extract_addon_type_two():
    """addon contains two top-levels, no nested folder outside"""
    zip_file = path.join(addon_src, 'addon_type_two.zip')
    copied_items = helpers.extract_to_dst(zip_file, addon_dst)
    assert len(copied_items) == 2, 'addon-type-two should contains two folder.'
    for i in copied_items:
        basename = path.basename(i)
        assert basename == 'addon_main' or basename == 'addon_sub', "addon-type-two's folder name should be addon_main or addon_sub."
        rmtree(i)

    cache_folder = path.join(cache_path, 'addon_type_two')
    assert not path.exists(cache_folder), 'cache should be remove after addon-type-two installed.'
    addon_main = path.join(addon_dst, 'addon_main')
    addon_sub = path.join(addon_dst, 'addon_sub')
    assert not path.exists(addon_main)
    assert not path.exists(addon_sub)

def test_extract_addon_type_three():
    """addon contains two top-levels, with nested folder outside"""
    zip_file = path.join(addon_src, 'addon_type_three.zip')
    copied_items = helpers.extract_to_dst(zip_file, addon_dst)
    assert len(copied_items) == 2, 'addon-type-three should contains two folder.'
    for i in copied_items:
        basename = path.basename(i)
        assert basename == 'addon_main' or basename == 'addon_sub', "inside addon-type-three nested folder, folder name should be addon_main or addon_sub."
        rmtree(i)

    cache_folder = path.join(cache_path, 'addon_type_three')
    assert not path.exists(cache_folder), 'cache should be remove after addon-type-three installed.'
    
def test_extract_addon_type_error():
    """addon contains both folders and files."""
    """it means that this is not a standard addon."""
    try:
        zip_file = path.join(addon_src, 'addon_type_error.zip')
        helpers.extract_to_dst(zip_file, addon_dst)
    except Exception as identifier:
        pass
    else:
        assert False, 'app should raise error when passing a error addon.'
    finally:
        cache_folder = path.join(cache_path, 'addon_type_error')
        addon_main = path.join(addon_dst, 'addon_main')
        addon_rdme = path.join(addon_dst, 'readme.md')
        assert not path.exists(cache_folder), 'cache should be remove after addon-type-error failed.'
        assert not path.exists(addon_main)
        assert not path.exists(addon_rdme)