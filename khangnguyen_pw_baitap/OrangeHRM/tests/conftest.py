import pytest
from utils.read_json import read_json

@pytest.fixture(scope="session")
def get_credentials():
    return read_json("resources/credentials.json")
