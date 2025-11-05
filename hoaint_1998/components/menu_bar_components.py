from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.base_component import BaseComponent

class MenuBarComponents(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.menu_home_button = BaseComponent.MENU_HOME_BUTTON
        self.menu_attendance_button = BaseComponent.MENU_ATTENDANCE_BUTTON
        self.menu_project_button = BaseComponent.MENU_PROJECT_BUTTON
        self.menu_tasks_button = BaseComponent.MENU_TASKS_BUTTON
        self.menu_payroll_button = BaseComponent.MENU_PAYROLL_BUTTON
        self.menu_request_button = BaseComponent.MENU_REQUEST_BUTTON
        self.menu_leave_request_button = BaseComponent.MENU_LEAVE_REQUEST_BUTTON
        self.menu_expense_claim_button = BaseComponent.MENU_EXPENSE_CLAIM_BUTTON
        self.menu_request_loan_button = BaseComponent.MENU_REQUEST_LOAN_BUTTON
        self.menu_travel_request_button = BaseComponent.MENU_TRAVEL_REQUEST_BUTTON
        self.menu_advance_salary_button = BaseComponent.MENU_ADVANCE_SALARY_BUTTON
        self.menu_overtime_request_button = BaseComponent.MENU_OVERTIME_REQUEST_BUTTON
        self.menu_helpdesk_button = BaseComponent.MENU_HELPDESK_BUTTON
        self.menu_training_session_button = BaseComponent.MENU_TRAINING_SESSIONS_BUTTON
        self.menu_employee_button = BaseComponent.MENU_EMPLOYEE_BUTTON
        self.menu_recruitment_ast_button = BaseComponent.MENU_RECRUITMENT_ATS_BUTTON
        self.menu_core_hr_button = BaseComponent.MENU_CORE_HR_BUTTON
        self.menu_deparment_button = BaseComponent.MENU_DEPARMENT_BUTTON
        self.menu_designation_button = BaseComponent.MENU_DESIGNATION_BUTTON
        self.menu_policies_button = BaseComponent.MENU_POLICIES_BUTTON
        self.menu_make_announcement_button = BaseComponent.MENU_MAKE_ANNOUNCEMENT_BUTTON
        self.menu_organization_chart_button = BaseComponent.MENU_ORGANIZATION_CHART_BUTTON
        self.menu_finance_button = BaseComponent.MENU_FINANCE_BUTTON
        self.menu_performance_pms_button = BaseComponent.MENU_PERFORMANCE_PMS_BUTTON
        self.menu_kpi_indicator_button = BaseComponent.MENU_KPI_INDICATOR_BUTTON
        self.menu_kpa_appraisal_button = BaseComponent.MENU_KPA_APPRAISAL_BUTTON
        self.menu_campetencies_button = BaseComponent.MENU_CAMPETENCIES_BUTTON
        self.menu_tract_goals_okrs_button = BaseComponent.MENU_TRACK_GOALS_OKRS_BUTTON
        self.menu_goal_type_button = BaseComponent.MENU_GOAL_TYPE_BUTTON
        self.menu_goals_calendar_button = BaseComponent.MENU_GOALS_CALENDAR_BUTTON
        self.menu_inventory_control_button = BaseComponent.MENU_INVENTORY_CONTOL_BUTTON
        self.menu_warehourses_button = BaseComponent.MENU_WAREHOUSES_BUTTON
        self.menu_product_button = BaseComponent.MENU_PRODUCTS_BUTTON
        self.menu_suppliers_button = BaseComponent.MENU_SUPPLIERS_BUTTON
        self.menu_purchases_button = BaseComponent.MENU_PURCHASES_BUTTON
        self.menu_sales_order_button = BaseComponent.MENU_SALES_ORDER_BUTTON
        self.menu_manage_clients_button = BaseComponent.MENU_MANAGE_CLIENTS_BUTTON
        self.menu_leads_button = BaseComponent.MENU_LEADS_BUTTON
        self.menu_invoices_button = BaseComponent.MENU_INVOICES_BUTTON
        self.menu_estimates_button = BaseComponent.MENU_ESTIMATES_BUTTON
        self.menu_disciplinary_cases_button = BaseComponent.MENU_DISCIPLINARY_CASES_BUTTON

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
    
