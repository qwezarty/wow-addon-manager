# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from wow_addon_manager.app import App

root_path = Path(__file__).parent.parent
app = App(__name__, root_path)

def test_config_from_mapping():
    app.system_config.from_mapping({
        'secret_key': 'devkey',
        'test_key': 'foo'
    })
    assert app.system_config['secret_key'] == 'devkey'
    assert app.system_config['test_key'] == 'foo'

def test_config_from_system_json_file():
    assert app.system_config['secret_key'] == 'devkey'

def test_config_from_user_json_file():
    assert app.user_config['source'] == 'curse'
    assert len(app.user_config['addons'])