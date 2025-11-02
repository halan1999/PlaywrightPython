from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from test_data.randoms import random_id
from test_data.project_information_storage import save_project_title
from test_data.project_data_loader import load_project_data
from test_data.credentials_loader import get_valid
import re

def test_create_project(page: Page):
    # Load credentials + project data
    username, password = get_valid()
    data = load_project_data()

    # Data combine
    uid = random_id()
    project_title = f"{data['project_title_prefix']} {uid}"
    client = data["client"]
    summary = data["summary"]
    start_day = data["start_day"]
    end_day = data["end_day"]

    save_project_title(project_title)

    # Steps
    LoginPage(page).open().login(username, password)
    projects = ProjectsPage(page).open_menu().click_add_new()
    projects.create_project(
        title=project_title,
        client_text=client,
        start_day=start_day,
        end_day=end_day,
        summary=summary
    ).search(project_title).hover_first_row()

    # Asserts
    expect(projects.first_row_title()).to_contain_text(project_title)
    expect(projects.first_row_client()).to_contain_text(client)
