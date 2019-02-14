# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from wow_addon_manager.app import App

app = App(__name__, Path(__file__).parent.parent)
app.system_config['run_mode'] == 'test'

def test_default_source():
    assert app.request.source_name == 'curseforge'

def test_change_source():
    app.request.change_source('wowinterface')
    assert app.request.source_name == 'wowinterface'

def test_curseforge_get_info():
    app.request.change_source('curseforge')
    addon = app.request.get_info('gtfo')
    assert addon['id'] == 'gtfo'
    assert addon['name'] == 'GTFO'
    assert addon['game_version'], 'game_version should not be None or empty.'
    assert addon['last_update'], 'last_update should not be None or empty.'
    assert addon['description'], 'description should not be None or empty.'
    assert addon['addon_url'], 'addon-url should not be None or empty.'
    assert addon['download_url'], 'download-url should not be None or empty.'
    assert addon['image'], 'image-url should not be None or empty.'
