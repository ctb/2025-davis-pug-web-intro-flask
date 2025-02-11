import os
import shutil

import pytest

from main import create_app

@pytest.fixture()
def app(tmp_path):
    app = create_app()

    # other setup can go here

    yield app
    
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
