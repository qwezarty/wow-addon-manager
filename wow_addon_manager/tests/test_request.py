# -*- coding: utf-8 -*-

import pytest
from wow_addon_manager.app import App

app = App(__name__)
app.config.from_json('../config/user.sample.json')

def test_search_addon():
