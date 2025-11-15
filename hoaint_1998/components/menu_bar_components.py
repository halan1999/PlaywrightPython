from playwright.sync_api import Page
from core.base_page import BasePage
from core.common_locators import CommonLocators

class MenuBarComponents(BasePage):
    MENU_HOME_BUTTON = CommonLocators._normalize_space_xpath("span", "Home")
    MENU_ATTENDANCE_BUTTON = CommonLocators._normalize_space_xpath("span", "Attendance")
    MENU_PROJECT_BUTTON = CommonLocators._normalize_space_xpath("span", "Projects")
    MENU_TASKS_BUTTON = CommonLocators._normalize_space_xpath("span", "Tasks")
    MENU_PAYROLL_BUTTON = CommonLocators._normalize_space_xpath("span", "Payroll")
    MENU_REQUEST_BUTTON = CommonLocators._normalize_space_xpath("a", "Requests")
    MENU_LEAVE_REQUEST_BUTTON = CommonLocators._normalize_space_xpath("a", "Leave Request")
    MENU_EXPENSE_CLAIM_BUTTON = CommonLocators._normalize_space_xpath("a", "Expense Claim")
    MENU_REQUEST_LOAN_BUTTON = CommonLocators._normalize_space_xpath("a", "Request Loan")
    MENU_TRAVEL_REQUEST_BUTTON = CommonLocators._normalize_space_xpath("a", "Travel Request")
    MENU_ADVANCE_SALARY_BUTTON = CommonLocators._normalize_space_xpath("a", "Advance Salary")
    MENU_OVERTIME_REQUEST_BUTTON = CommonLocators._normalize_space_xpath("a", "Overtime Request")
    MENU_HELPDESK_BUTTON = CommonLocators._normalize_space_xpath("span", "Helpdesk")
    MENU_TRAINING_SESSION_BUTTON = CommonLocators._normalize_space_xpath("span", "Training Sessions")
    MENU_EMPLOYEE_BUTTON = CommonLocators._normalize_space_xpath("span", "Employees")
    MENU_RECRUITMENT_ATS_BUTTON = CommonLocators._normalize_space_xpath("span", "Recruitment (ATS)")
    MENU_CORE_HR_BUTTON = CommonLocators._normalize_space_xpath("a", "Core HR")
    MENU_DEPARTMENT_BUTTON = CommonLocators._normalize_space_xpath("a", "Department")
    MENU_DESIGNATION_BUTTON = CommonLocators._normalize_space_xpath("a", "Designation")
    MENU_POLICIES_BUTTON = CommonLocators._normalize_space_xpath("a", "Policies")
    MENU_MAKE_ANNOUNCEMENT_BUTTON = CommonLocators._normalize_space_xpath("a", "Make Announcement")
    MENU_ORGANIZATION_CHART_BUTTON = CommonLocators._normalize_space_xpath("a", "Organization Chart")
    MENU_FINANCE_BUTTON = CommonLocators._normalize_space_xpath("span", "Finance")
    MENU_PERFORMANCE_PMS_BUTTON = CommonLocators._normalize_space_xpath("a", "Performance (PMS)")
    MENU_KPI_INDICATOR_BUTTON = CommonLocators._normalize_space_xpath("a", "KPI (Indicator)")
    MENU_KPA_APPRAISAL_BUTTON = CommonLocators._normalize_space_xpath("a", "KPA (Appraisal)")
    MENU_COMPETENCIES_BUTTON = CommonLocators._normalize_space_xpath("a", "Competencies")
    MENU_TRACK_GOALS_OKRS_BUTTON = CommonLocators._normalize_space_xpath("a", "Track Goals (OKRs)")
    MENU_GOAL_TYPE_BUTTON = CommonLocators._normalize_space_xpath("a", "Goal Type")
    MENU_GOALS_CALENDAR_BUTTON = CommonLocators._normalize_space_xpath("a", "Goals Calendar")
    MENU_INVENTORY_CONTROL_BUTTON = CommonLocators._normalize_space_xpath("span", "Inventory Control")
    MENU_WAREHOUSES_BUTTON = CommonLocators._normalize_space_xpath("a", "Warehouses")
    MENU_PRODUCT_BUTTON = "//a[@href='#!'][normalize-space()='Products']"
    MENU_SUPPLIERS_BUTTON = CommonLocators._normalize_space_xpath("a", "Suppliers")
    MENU_PURCHASES_BUTTON = CommonLocators._normalize_space_xpath("a", "Purchases")
    MENU_SALES_ORDER_BUTTON = CommonLocators._normalize_space_xpath("a", "Sales Order")
    MENU_MANAGE_CLIENTS_BUTTON = CommonLocators._normalize_space_xpath("span", "Manage Clients")
    MENU_LEADS_BUTTON = CommonLocators._normalize_space_xpath("span", "Leads")
    MENU_INVOICES_BUTTON = CommonLocators._normalize_space_xpath("span", "Invoices")
    MENU_ESTIMATES_BUTTON = CommonLocators._normalize_space_xpath("span", "Estimates")
    MENU_DISCIPLINARY_CASES_BUTTON = CommonLocators._normalize_space_xpath("span", "Disciplinary Cases")


    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _click_and_take_screenshot_all_button_in_menu(self):
        list_menu_buttons = [
            (self.MENU_HOME_BUTTON, "self.menu_home_button"),
            (self.MENU_ATTENDANCE_BUTTON, "self.menu_attendance_button"),
            (self.MENU_PROJECT_BUTTON, "self.menu_project_button"),
            (self.MENU_TASKS_BUTTON, "self.menu_tasks_button"),
            (self.MENU_PAYROLL_BUTTON, "self.menu_payroll_button"),
            (self.MENU_REQUEST_BUTTON, "self.menu_request_button"),
            (self.MENU_HELPDESK_BUTTON, "self.menu_helpdesk_button"),
            (self.MENU_TRAINING_SESSION_BUTTON, "self.menu_training_session_button"),
            (self.MENU_EMPLOYEE_BUTTON, "self.menu_employee_button"),
            (self.MENU_RECRUITMENT_ATS_BUTTON, "self.menu_recruitment_ast_button"),
            (self.MENU_CORE_HR_BUTTON, "self.menu_core_hr_button"),
            (self.MENU_FINANCE_BUTTON, "self.menu_finance_button"),
            (self.MENU_PERFORMANCE_PMS_BUTTON, "self.menu_performance_pms_button"),
            (self.MENU_INVENTORY_CONTROL_BUTTON, "self.menu_inventory_control_button"),
            (self.MENU_MANAGE_CLIENTS_BUTTON, "self.menu_manage_clients_button"),
            (self.MENU_LEADS_BUTTON, "self.menu_leads_button"),
            (self.MENU_INVOICES_BUTTON, "self.menu_invoices_button"),
            (self.MENU_ESTIMATES_BUTTON, "self.menu_estimates_button"),
            (self.MENU_DISCIPLINARY_CASES_BUTTON, "self.menu_disciplinary_cases_button"),
        ]
        for locator, title in list_menu_buttons:
            self._click(locator)
            self._take_screenshot(title)
            self.page.wait_for_timeout(300)
    
