from playwright.sync_api import Page, expect

class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page

    # ===== Locators =====
    _menu_projects = "//div[@class='navbar-wrapper']//a[contains(@href,'projects-list')]"
    _add_new_btn   = "//a[@href='#add_form' and contains(normalize-space(.), 'Add New')]"

    _title_input   = "//input[@name='title' and @type='text']"
    _client_select = "#client_id"
    _start_input   = "//input[@name='start_date']"
    _end_input     = "//input[@name='end_date']"
    _summary_text  = "//textarea[@id='summary']"
    _save_btn      = "//div[@class='card-footer text-right']//button[@type='submit']"

    _table_search  = "//div[@id='xin_table_wrapper']//input[@type='search']"
    _first_row     = "//table[@id='xin_table']/tbody/tr[@role='row'][1]"
    _first_cell    = "//table[@id='xin_table']/tbody/tr[@role='row'][1]/td[1]"
    _second_cell   = "//table[@id='xin_table']/tbody/tr[@role='row'][1]/td[2]"

    # ===== Actions =====
    def open_menu(self) -> "ProjectsPage":
        self.page.locator(self._menu_projects).click()
        self.page.wait_for_selector(self._add_new_btn)
        return self

    def click_add_new(self) -> "ProjectsPage":
        self.page.locator(self._add_new_btn).click()
        self.page.wait_for_selector(self._title_input)
        return self

    def _pick_day_in_open_calendar(self, day: str):
        self.page.locator("div.dtp:visible .dtp-select-day", has_text=day).click()
        self.page.locator("div.dtp:visible button.dtp-btn-ok").click()

    def create_project(self, title: str, client_text: str, start_day: str, end_day: str, summary: str) -> "ProjectsPage":
        self.page.locator(self._title_input).fill(title)
        self.page.locator(self._client_select).select_option(label=client_text)

        self.page.locator(self._start_input).click()
        self._pick_day_in_open_calendar(start_day)

        self.page.locator(self._end_input).click()
        self._pick_day_in_open_calendar(end_day)

        self.page.locator(self._summary_text).fill(summary)
        self.page.locator(self._save_btn).click()

        # quay về list
        self.page.wait_for_selector(self._table_search)
        return self

    def search(self, keyword: str) -> "ProjectsPage":
        self.page.locator(self._table_search).fill(keyword)
        return self

    def first_row_title(self):
        return self.page.locator(self._first_cell)

    def first_row_client(self):
        return self.page.locator(self._second_cell)

    def hover_first_row(self):
        self.page.locator(self._first_row).hover()
