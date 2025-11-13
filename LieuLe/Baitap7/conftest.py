import pytest
from playwright.sync_api import Playwright

#1. Launch browser (headed = false)
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    

