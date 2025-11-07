from playwright.sync_api import Page
from core.base_page import BasePage
from core.common_locators import CommonLocators

class MenuBarComponents(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.menu_home_button = CommonLocators._normalize_space_xpath("span", "Home")
        self.menu_attendance_button = CommonLocators._normalize_space_xpath("span", "Attendance")
        self.menu_project_button = CommonLocators._normalize_space_xpath("span", "Projects")
        self.menu_tasks_button = CommonLocators._normalize_space_xpath("span", "Tasks")
        self.menu_payroll_button = CommonLocators._normalize_space_xpath("span", "Payroll")
        self.menu_request_button = CommonLocators._normalize_space_xpath("a", "Requests")
        self.menu_leave_request_button = CommonLocators._normalize_space_xpath("a", "Leave Request")
        self.menu_expense_claim_button = CommonLocators._normalize_space_xpath("a", "Expense Claim")
        self.menu_request_loan_button = CommonLocators._normalize_space_xpath("a", "Request Loan")
        self.menu_travel_request_button = CommonLocators._normalize_space_xpath("a", "Travel Request")
        self.menu_advance_salary_button = CommonLocators._normalize_space_xpath("a", "Advance Salary")
        self.menu_overtime_request_button = CommonLocators._normalize_space_xpath("a", "Overtime Request")
        self.menu_helpdesk_button = CommonLocators._normalize_space_xpath("span", "Helpdesk")
        self.menu_training_session_button = CommonLocators._normalize_space_xpath("span", "Training Sessions")
        self.menu_employee_button = CommonLocators._normalize_space_xpath("span", "Employees")
        self.menu_recruitment_ast_button = CommonLocators._normalize_space_xpath("span", "Recruitment (ATS)")
        self.menu_core_hr_button = CommonLocators._normalize_space_xpath("a", "Core HR")
        self.menu_deparment_button = CommonLocators._normalize_space_xpath("a", "Department")
        self.menu_designation_button = CommonLocators._normalize_space_xpath("a", "Designation")
        self.menu_policies_button = CommonLocators._normalize_space_xpath("a", "Policies")
        self.menu_make_announcement_button = CommonLocators._normalize_space_xpath("a", "Make Announcement")
        self.menu_organization_chart_button = CommonLocators._normalize_space_xpath("a", "Organization Chart")
        self.menu_finance_button =CommonLocators._normalize_space_xpath("span", "Finance")
        self.menu_performance_pms_button = CommonLocators._normalize_space_xpath("a", "Performance (PMS)")
        self.menu_kpi_indicator_button = CommonLocators._normalize_space_xpath("a", "KPI (Indicator)")
        self.menu_kpa_appraisal_button = CommonLocators._normalize_space_xpath("a", "KPA (Appraisal)")
        self.menu_campetencies_button = CommonLocators._normalize_space_xpath("a", "Competencies")
        self.menu_tract_goals_okrs_button = CommonLocators._normalize_space_xpath("a", "Track Goals (OKRs)")
        self.menu_goal_type_button = CommonLocators._normalize_space_xpath("a", "Goal Type")
        self.menu_goals_calendar_button = CommonLocators._normalize_space_xpath("a", "Goals Calendar")
        self.menu_inventory_control_button = CommonLocators._normalize_space_xpath("span", "Inventory Control")
        self.menu_warehourses_button = CommonLocators._normalize_space_xpath("a", "Warehouses")
        self.menu_product_button = "//a[@href='#!'][normalize-space()='Products']"
        self.menu_suppliers_button = CommonLocators._normalize_space_xpath("a", "Suppliers")
        self.menu_purchases_button = CommonLocators._normalize_space_xpath("a", "Purchases")
        self.menu_sales_order_button = CommonLocators._normalize_space_xpath("a", "Sales Order")
        self.menu_manage_clients_button = CommonLocators._normalize_space_xpath("span", "Manage Clients")
        self.menu_leads_button = CommonLocators._normalize_space_xpath("span", "Leads")
        self.menu_invoices_button = CommonLocators._normalize_space_xpath("span", "Invoices")
        self.menu_estimates_button = CommonLocators._normalize_space_xpath("span", "Estimates")
        self.menu_disciplinary_cases_button = CommonLocators._normalize_space_xpath("span", "Disciplinary Cases")

    def _click_and_take_screenshot_all_button_in_menu(self):
        list_menu_buttons = [
            (self.menu_home_button, "self.menu_home_button"),
            (self.menu_attendance_button, "self.menu_attendance_button"),
            (self.menu_project_button, "self.menu_project_button"),
            (self.menu_tasks_button, "self.menu_tasks_button"),
            (self.menu_payroll_button, "self.menu_payroll_button"),
            (self.menu_request_button, "self.menu_request_button"),
            # (self.menu_leave_request_button, "self.menu_leave_request_button"),
            # (self.menu_expense_claim_button, "self.menu_expense_claim_button"),
            # (self.menu_request_loan_button, "self.menu_request_loan_button"),
            # (self.menu_travel_request_button, "self.menu_travel_request_button"),
            # (self.menu_advance_salary_button, "self.menu_advance_salary_button"),
            # (self.menu_overtime_request_button, "self.menu_overtime_request_button"),
            (self.menu_helpdesk_button, "self.menu_helpdesk_button"),
            (self.menu_training_session_button, "self.menu_training_session_button"),
            (self.menu_employee_button, "self.menu_employee_button"),
            (self.menu_recruitment_ast_button, "self.menu_recruitment_ast_button"),
            (self.menu_core_hr_button, "self.menu_core_hr_button"),
            # (self.menu_deparment_button, "self.menu_deparment_button"),
            # (self.menu_designation_button, "self.menu_designation_button"),
            # (self.menu_policies_button, "self.menu_policies_button"),
            # (self.menu_make_announcement_button, "self.menu_make_announcement_button"),
            # (self.menu_organization_chart_button, "self.menu_organization_chart_button"),
            (self.menu_finance_button, "self.menu_finance_button"),
            (self.menu_performance_pms_button, "self.menu_performance_pms_button"),
            # (self.menu_kpi_indicator_button, "self.menu_kpi_indicator_button"),
            # (self.menu_kpa_appraisal_button, "self.menu_kpa_appraisal_button"),
            # (self.menu_campetencies_button, "self.menu_campetencies_button"),
            # (self.menu_tract_goals_okrs_button, "self.menu_tract_goals_okrs_button"),
            # (self.menu_goal_type_button, "self.menu_goal_type_button"),
            # (self.menu_goals_calendar_button, "self.menu_goals_calendar_button"),
            (self.menu_inventory_control_button, "self.menu_inventory_control_button"),
            # (self.menu_warehourses_button, "self.menu_warehourses_button"),
            # (self.menu_product_button, "self.menu_product_button"),
            # (self.menu_suppliers_button, "self.menu_suppliers_button"),
            # (self.menu_purchases_button, "self.menu_purchases_button"),
            # (self.menu_sales_order_button, "self.menu_sales_order_button"),
            (self.menu_manage_clients_button, "self.menu_manage_clients_button"),
            (self.menu_leads_button, "self.menu_leads_button"),
            (self.menu_invoices_button, "self.menu_invoices_button"),
            (self.menu_estimates_button, "self.menu_estimates_button"),
            (self.menu_disciplinary_cases_button, "self.menu_disciplinary_cases_button"),
        ]
        for locator, title in list_menu_buttons:
            self._click(locator)
            self._take_screenshot(title)
            self.page.wait_for_timeout(300)
    
