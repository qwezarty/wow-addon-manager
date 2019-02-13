# -*- coding: utf-8 -*-

from wow_addon_manager.app import App
from pathlib import Path
from os import path
from shutil import rmtree

root_path = Path(__file__).parent.parent
app = App(__name__, root_path)

def test_init_dirs():
    interface_dir = path.join(root_path, 'tests', 'dst', 'Interface')
    app.addons_dir = path.join(interface_dir, 'Addons')
    cache_path = path.join(root_path, 'cache')
    if path.exists(cache_path):
        rmtree(cache_path)
    if path.exists(interface_dir):
        rmtree(interface_dir)

    app.init_dirs()

    assert path.exists(app.addons_dir), 'addons folder should be exist after init dirs.'
    assert path.exists(cache_path), 'cache folder should be exist after init dirs.'

    rmtree(cache_path)
    rmtree(interface_dir)