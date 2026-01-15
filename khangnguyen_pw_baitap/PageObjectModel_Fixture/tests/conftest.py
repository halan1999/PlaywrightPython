import json
import shutil
from pathlib import Path

import pytest
from playwright.sync_api import APIRequestContext, Playwright

BOOK_URL = "https://book.anhtester.com/"

# Project root dir (../ from tests/)
ROOT_DIR = Path(__file__).resolve().parent.parent

# resources/saucedemo/credentials_parallel.json
CREDENTIALS_FILE = ROOT_DIR / "resources" / "saucedemo" / "credentials_parallel.json"

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(
        base_url=BOOK_URL,
        extra_http_headers={"Content-Type": "application/json"},
    )
    try:
        yield context
    finally:
        context.dispose()


@pytest.fixture(scope="session")
def browser_context_args() -> dict:
    return {"viewport": {"width": 1600, "height": 900}}


@pytest.fixture(scope="session")
def credentials() -> list[dict]:
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(f"Credentials file not found: {CREDENTIALS_FILE}")

    with open(CREDENTIALS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    users = data.get("users")
    if not isinstance(users, list):
        raise ValueError("Invalid credentials schema: expected key 'users' as a list")

    return users


@pytest.fixture(scope="session", autouse=True)
def clean_allure_folders() -> None:
    results_dir = ROOT_DIR / "allure-results"
    report_dir = ROOT_DIR / "allure-report"

    for folder in (results_dir, report_dir):
        if folder.exists():
            shutil.rmtree(folder)

    # make sure allure-results exists before pytest writes into it
    results_dir.mkdir(parents=True, exist_ok=True)