import shutil
import json
import pytest
from pathlib import Path

# root = PAGEOBJECTMODEL_FIXTURE
ROOT_DIR = Path(__file__).resolve().parent.parent

# resources/saucedemo/credentials_parallel.json
CREDENTIALS_FILE = (
    ROOT_DIR / "resources" / "saucedemo" / "credentials_parallel.json"
)

# Playwright context config
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1600, "height": 900}
    }

# Load credentials ONCE per session
@pytest.fixture(scope="session")
def credentials():
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(
            f"Credentials file not found: {CREDENTIALS_FILE}"
        )

    with open(CREDENTIALS_FILE, encoding="utf-8") as f:
        return json.load(f)["users"]

@pytest.fixture(scope="session", autouse=True)
def clean_allure_folders():
    results_dir = ROOT_DIR / "allure-results"
    report_dir = ROOT_DIR / "allure-report"

    # remove folders if exist
    for folder in [results_dir, report_dir]:
        if folder.exists():
            shutil.rmtree(folder)

    # recreate allure-results so pytest can write into it
    results_dir.mkdir(parents=True, exist_ok=True)