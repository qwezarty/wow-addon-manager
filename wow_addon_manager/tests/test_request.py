# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from wow_addon_manager.app import App

app = App(__name__, Path(__file__).parent.parent)

def test_search_addon():
    pass