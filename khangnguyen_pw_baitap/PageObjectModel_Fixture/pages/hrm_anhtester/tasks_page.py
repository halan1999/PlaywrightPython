from playwright.sync_api import Page, Locator, expect


class TasksPage:
    header_items = {
        "tasks": '//a[contains(@href, "tasks-grid")]',
        "calendar": '//a[contains(@href, "tasks-calendar")]',
        "kanban": '//a[contains(@href, "tasks-scrum-board")]',
    }

    # Locators - Tasks page
    menu_tasks = '//span[normalize-space()="Tasks"]'
    add_new_btn = '//a[normalize-space()="Add Task"]'

    title_field = '//input[@name="task_name" and @type="text"]'
    startdate_field = '//input[@name="start_date"]'
    enddate_field = '//input[@name="end_date"]'
    project_field = '//select[@name="project_id"]'
    search_project_field = '//input[@type="search" and @role="searchbox"]'
    summary_text = '//textarea[@id="summary"]'
    save_btn = '//button[@type="submit"]'

    search_field = '//input[@type="search"]'
    first_cell = '//table[@id="xin_table"]/tbody/tr[1]/td[1]'

    # Calendar locators
    calendar_root = '(//div[contains(@class,"dtp")])[last()]'
    calendar_date_view = calendar_root + '//div[contains(@class,"dtp-date-view")]'
    calendar_ok_button = calendar_root + '//button[contains(@class,"dtp-btn-ok")]'
    calendar_table = calendar_root + '//table[contains(@class,"dtp-picker-days")]'
    calendar_view = '//div[@id="calendar_hr"]'

    def __init__(self, page: Page):
        self.page: Page = page

    # Open Tasks menu
    def click_menu(self):
        self.page.click(self.menu_tasks)
        return self

    # Click Add New button (giữ nguyên tên function)
    def click_add_new(self):
        self.page.click(self.add_new_btn)
        return self

    # Create a new task
    def create_task(
        self,
        taskTitle: str,
        taskStartDate: str,
        taskEndDate: str,
        taskSummary: str,
        taskClient: str,
    ):

        # Input task title
        self.page.fill(self.title_field, taskTitle)

        # Select task client
        self.page.select_option(self.project_field, label=taskClient)

        # Open start date calendar and pick a date
        self._open_calendar(self.startdate_field)
        self._pick_day(taskStartDate)

        # Open end date calendar and pick a date
        self._open_calendar(self.enddate_field)
        self._pick_day(taskEndDate)

        # Input task summary
        self.page.fill(self.summary_text, taskSummary)

        # Click Save button
        self.page.click(self.save_btn)

        # Wait search field displayed on the table after adding a task
        self.page.locator(self.search_field).wait_for(state="visible")
        return self

    def is_tasks_page_loaded(self):
        expect(self.page.locator(self.header_items["tasks"]).first).to_be_visible(timeout=5000)
        expect(self.page.locator(self.header_items["calendar"]).first).to_be_visible(timeout=5000)
        expect(self.page.locator(self.header_items["kanban"]).first).to_be_visible(timeout=5000)

        return self

    def click_header_item(self, name: str):
        locator = self.header_items.get(name.lower())
        element = self.page.locator(locator).first
        expect(element).to_be_visible(timeout=5000)
        element.click()

        return self

    # ===== Helper functions (private) =====

    def _open_calendar(self, input_selector: str) -> None:
        self.page.click(input_selector)
        self.page.locator(self.calendar_date_view).wait_for(state="visible")

    def _pick_day(self, day_text: str) -> None:
        table = self.page.locator(self.calendar_table)
        expect(table).to_be_visible()

        # Click valid day cell, not old/new month
        self.page.locator(
            f'{self.calendar_table}//td[not(contains(@class,"old")) and not(contains(@class,"new"))]'
            f'//div[normalize-space()="{day_text}"]'
        ).click()

        # Confirm
        self.page.click(self.calendar_ok_button)
        self.page.wait_for_timeout(200)
