from playwright.sync_api import Page, Locator, expect


class ProjectsPage():
    _menu_projects = '//a[contains(@href,"projects-list")]'
    _add_new_btn = '//a[@href="#add_form" and contains(normalize-space(.),"Add New")]'

    _title_field = '//input[@name="title" and @type="text"]'
    _client_select = '//select[@id="client_id"]'
    _startdate_field = '//input[@name="start_date"]'
    _enddate_field = '//input[@name="end_date"]'
    _summary_text = '//textarea[@id="summary"]'
    _save_btn = '//button[@type="submit"]'

    _search_field = '//input[@type="search"]'
    _first_cell = '//table[@id="xin_table"]/tbody/tr[1]/td[1]'

    # Calendar locators
    _calendar_root = '(//div[contains(@class,"dtp")])[last()]'
    _calendar_view = _calendar_root + '//div[contains(@class,"dtp-date-view")]'
    _calendar_ok_button = _calendar_root + '//button[contains(@class,"dtp-btn-ok")]'
    _calendar_table = _calendar_root + '//table[contains(@class,"dtp-picker-days")]'

    def __init__(self, page: Page):
        self.page: Page = page

    # Open Projects menu
    def click_menu(self):
        self.page.click(self._menu_projects)
        return self

    # Click Add New button (giữ nguyên tên function)
    def click_add_new(self):
        self.page.click(self._add_new_btn)
        return self

    # Create a new project
    def create_project(
        self,
        projectTitle: str,
        projectClient: str,
        projectStartDate: str,
        projectEndDate: str,
        projectSummary: str,
    ):

        # Input project title
        self.page.fill(self._title_field, projectTitle)

        # Select project client
        self.page.select_option(self._client_select, label=projectClient)

        # Open start date calendar and pick a date
        self._open_calendar(self._startdate_field)
        self._pick_day(projectStartDate)

        # Open end date calendar and pick a date
        self._open_calendar(self._enddate_field)
        self._pick_day(projectEndDate)

        # Input project summary
        self.page.fill(self._summary_text, projectSummary)

        # Click Save button
        self.page.click(self._save_btn)

        # Wait search field displayed on the table after adding a project
        self.page.locator(self._search_field).wait_for(state="visible")
        return self

    # Search created project
    def search_created_project(self, keyword: str):
        self.page.fill(self._search_field, keyword)
        return self

    # Get first cell for assertion
    def get_first_cell(self) -> Locator:
        return self.page.locator(self._first_cell)

    # ===== Helper functions (private) =====

    def _open_calendar(self, input_selector: str) -> None:
        self.page.click(input_selector)
        self.page.locator(self._calendar_view).wait_for(state="visible")

    def _pick_day(self, day_text: str) -> None:
        table = self.page.locator(self._calendar_table)
        expect(table).to_be_visible()

        # Click valid day cell, not old/new month
        self.page.locator(
            f'{self._calendar_table}//td[not(contains(@class,"old")) and not(contains(@class,"new"))]'
            f'//div[normalize-space()="{day_text}"]'
        ).click()

        # Confirm
        self.page.click(self._calendar_ok_button)
        self.page.wait_for_timeout(200)
