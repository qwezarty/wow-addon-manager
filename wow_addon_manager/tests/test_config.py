# -*- coding: utf-8 -*-

import pytest
from wow_addon_manager.app import App

def test_config_from_mapping():
    app = App(__name__)

    app.config.from_mapping({
        'secret_key': 'devkey',
        'test_key': 'foo'
    })

    assert app.config['secret_key'] == 'devkey'
    assert app.config['test_key'] == 'foo'

def test_config_from_system_json_file():
    app = App(__name__)
    app.config.from_json('../config/system.json')
    assert app.config['secret_key'] == 'devkey'

def test_config_from_user_json_file():
    app = App(__name__)
    app.config.from_json('../config/user.sample.json')
    assert app.config['source'] == 'curse'
    assert len(app.config['addons'])