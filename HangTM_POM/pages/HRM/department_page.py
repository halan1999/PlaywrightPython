from playwright.async_api import Page
from Core.Base_page import BasePage

class DepartmentPage(BasePage):
    URL="https://hrm.anhtester.com/erp/departments-list"
    def __init__(self, page):
        super().__init__(page)
        #Menu locators:
        self.core_hr_menu="//a[contains(normalize-space(.), 'Core HR')]"
        self.department_menu="//a[contains(@href, '/erp/departments-list')]"
        #Form Add Department locators:
        self.name_input="input[name='department_name']"
        self.save_button="//span[contains(normalize-space(.), 'Save')]/parent::button"
        #search + table locators:
        self.search_input="input[type='search']"
        self.table_rows="table#xin_table tbody tr"
    def open_department_page(self) -> None:
        self.click(self.core_hr_menu)
        self.click(self.department_menu)
        self.should_visible(self.name_input)
    def add_department(self, name:str) -> None:
        self.fill(self.name_input,name)
        self.click(self.save_button)
        self.should_visible(self.table_rows)
    def search_department(self, name:str) ->None:
        self.fill(self.search_input,name)
    def is_department_present(self, name:str)->bool:
       rows=self.page.locator(self.table_rows)
       return rows.filter(has_text=name).count()>0
