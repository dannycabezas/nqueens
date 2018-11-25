"""conftest module."""

import json

from collections import OrderedDict

import pytest


@pytest.fixture
def get_resource(shared_datadir):

    def _get_resource(filename):
        shared_filename = shared_datadir / filename
        event = {}
        if shared_filename.exists() and shared_filename.is_file():
            with shared_filename.open() as sf:
                event = json.loads(sf.read(), object_pairs_hook=OrderedDict)
        return event

    return _get_resource
