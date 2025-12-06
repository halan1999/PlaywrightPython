from pathlib import Path
import json
from playwright.sync_api import Page, Locator, expect


class TasksPage():
    def __init__(self, page: Page):
        self.page: Page = page


        self.HEADER_ITEMS = {
            "tasks": '//a[contains(@href, "tasks-grid")]',
            "calendar": '//a[contains(@href, "tasks-calendar")]',
            "kanban": '//a[contains(@href, "tasks-scrum-board")]'
        }

        # Locators - Tasks page

        self._add_task_button = '//a[normalize-space()="Add Task"]'

        self._title_field = '//input[@name="task_name" and @type="text"]'
        self._startdate_field = '//input[@name="start_date"]'
        self._enddate_field = '//input[@name="end_date"]'
        self._project_field = '//select[@name="project_id"]'
        self._search_project_field = '//input[@type="search" and @role="searchbox"]'
        self._summary_text = '//textarea[@id="summary"]'
        self._save_btn = '//button[@type="submit"]'

        self._search_field = '//input[@type="search"]'
        self._first_cell = '//table[@id="xin_table"]/tbody/tr[1]/td[1]'

        # Calendar locators
        self._calendar_root = '(//div[contains(@class,"dtp")])[last()]'
        self._calendar_view = self._calendar_root + '//div[contains(@class,"dtp-date-view")]'
        self._calendar_ok_button = self._calendar_root + '//button[contains(@class,"dtp-btn-ok")]'
        self._calendar_table = self._calendar_root + '//table[contains(@class,"dtp-picker-days")]'

        # Locators - Calendar
        self._calendar_view = '//div[@id="calendar_hr"]'

    # Open Tasks menu
    def click_menu(self):
        self.page.click(self._menu_Tasks)
        return self

    # Click Add New button (giữ nguyên tên function)
    def click_add_new(self):
        self.page.click(self._add_new_btn)
        return self

    # Create a new task
    def create_task(
        self,
        taskTitle: str,
        taskStartDate: str,
        taskEndDate: str,
        taskSummary: str,
    ):

        # Input task title
        self.page.fill(self._title_field, taskTitle)

        # Select task client
        self.page.select_option(self._client_select, label=taskClient)

        # Open start date calendar and pick a date
        self._open_calendar(self._startdate_field)
        self._pick_day(taskStartDate)

        # Open end date calendar and pick a date
        self._open_calendar(self._enddate_field)
        self._pick_day(taskEndDate)

        # Input task summary
        self.page.fill(self._summary_text, taskSummary)

        # Click Save button
        self.page.click(self._save_btn)

        # Wait search field displayed on the table after adding a task
        self.page.locator(self._search_field).wait_for(state="visible")
        return self

    def is_tasks_page_loaded(self):
        expect(self.page.locator(self.HEADER_ITEMS["tasks"]).first).to_be_visible(timeout=5000)
        expect(self.page.locator(self.HEADER_ITEMS["calendar"]).first).to_be_visible(timeout=5000)
        expect(self.page.locator(self.HEADER_ITEMS["kanban"]).first).to_be_visible(timeout=5000)

        return self

    def click_header_item(self, name: str):
        locator = self.HEADER_ITEMS.get(name.lower())
        element = self.page.locator(locator).first
        expect(element).to_be_visible(timeout=5000)
        element.click()

        return self

