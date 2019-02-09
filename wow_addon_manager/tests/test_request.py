# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from wow_addon_manager.app import App

app = App(__name__, Path(__file__).parent.parent)

def test_default_source():
    assert app.request.source_name == 'curseforge'

def test_change_source():
    app.request.change_source('wowinterface')
    assert app.request.source_name == 'wowinterface'