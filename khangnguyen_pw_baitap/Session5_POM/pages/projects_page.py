from playwright.sync_api import Page, expect

class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    _menu_projects = '//div[@class="navbar-wrapper"]//a[contains(@href,"projects-list")]'
    _add_new_btn   = '//a[@href="#add_form" and contains(normalize-space(.), "Add New")]'
    _title_input   = '//input[@name="title" and @type="text"]'
    _client_select = '#client_id'
    _startdate_input  = '//input[@name="start_date"]'
    _enddate_input     = '//input[@name="end_date"]'
    _summary_text  = '//textarea[@id="summary"]'
    _save_btn      = '//div[@class="card-footer text-right"]//button[@type="submit"]'
    _search_field  = '//div[@id="xin_table_wrapper"]//input[@type="search"]'
    _first_row     = '//table[@id="xin_table"]/tbody/tr[@role="row"][1]'
    _first_cell    = '//table[@id="xin_table"]/tbody/tr[@role="row"][1]/td[1]'
    _second_cell   = '//table[@id="xin_table"]/tbody/tr[@role="row"][1]/td[2]'


    # Method: open Projects menu
    def open_menu(self) -> "ProjectsPage":
        self.page.locator(self._menu_projects).click()
        self.page.wait_for_selector(self._add_new_btn)
        return self

    # Method: click Add New button
    def click_add_new(self) -> "ProjectsPage":
        self.page.locator(self._add_new_btn).click()
        self.page.wait_for_selector(self._title_input)
        return self

    # Method: pick start date & end date
    def _pick_day_in_open_calendar(self, day: str):
        self.page.locator("div.dtp:visible .dtp-select-day", has_text=day).click()
        self.page.locator("div.dtp:visible button.dtp-btn-ok").click()

    # Method: create new project
    def create_project(self, title: str, client_text: str, start_day: str, end_day: str, summary: str) -> "ProjectsPage":
        self.page.locator(self._title_input).fill(title)
        self.page.locator(self._client_select).select_option(label=client_text)

        self.page.locator(self._start_input).click()
        self._pick_day_in_open_calendar(start_day)

        self.page.locator(self._enddate_input).click()
        self._pick_day_in_open_calendar(end_day)

        self.page.locator(self._summary_text).fill(summary)
        self.page.locator(self._save_btn).click()

        # Back to projects table
        self.page.wait_for_selector(self._search_field)
        return self

    # Method: search the newly created project
    def search(self, keyword: str) -> "ProjectsPage":
        self.page.locator(self._search_field).fill(keyword)
        return self

    # Method: get title
    def first_row_title(self):
        return self.page.locator(self._first_cell)

    # Method: get client
    def first_row_client(self):
        return self.page.locator(self._second_cell)

    # Method: hover first row of table
    def hover_first_row(self):
        self.page.locator(self._first_row).hover()
