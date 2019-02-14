# -*- coding: utf-8 -*-

from wow_addon_manager.app import App
from pathlib import Path
from os import path, remove
from shutil import rmtree, copy2

root_path = Path(__file__).parent.parent
app = App(__name__, root_path)
app.system_config['run_mode'] == 'test'

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

def test_get_user_config_path():
    user_sample_json = path.join(root_path, 'configs', 'user.sample.json')
    user_json = path.join(root_path, 'configs', 'user.json')
    if not path.exists(user_json):
        copy2(user_sample_json, user_json)
    result = app.get_user_config_path()
    assert path.exists(result) and result == user_json, 'if user.json exists, app should load user-config from it.'
    remove(user_json)
    result = app.get_user_config_path()
    assert path.exists(result) and result == user_sample_json, 'if user.json not exists, app should load user-sample-config from it.'
