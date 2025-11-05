from locators.common_locators import CommonLocators

class BaseComponent(CommonLocators):
    # -----------------------------
    # --------- HEADER ------------
    HEADER_LOGO = "//div[@class='header-wrapper']//a[contains(@href, 'desk')]"
    HEADER_ACCOUNT_SETTING_ICON = CommonLocators._attribute_data_original_title_xpath("a", "Account Settings")
    HEADER_APPS_ICON = CommonLocators._attribute_data_original_title_xpath("span", "Apps")
    HEADER_SYSTEM_CALENDAR = CommonLocators._attribute_data_original_title_xpath("a", "System Calendar")
    HEADER_SYSTEM_REPORTS = CommonLocators._attribute_data_original_title_xpath("a", "System Reports")
    HEADER_CHOOSE_LANGUAGE_ICON = "//div[@class='ml-auto']//li[1]"
    HEADER_TODO_LIST_ICON = CommonLocators._attribute_data_original_title_xpath("a", "Todo List")
    HEADER_AVATAR_ICON = "//div[@class='ml-auto']//li[3]"
    HEADER_MY_ACCOUNT_BUTTON = CommonLocators._contains_text_xpath("span", "My Account")
    HEADER_LOGOUT_BUTTON = CommonLocators._contains_text_xpath("span", "Logout")
    # -----------------------------
    # --------- MENU ------------
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
    MENU_TRAINING_SESSIONS_BUTTON = CommonLocators._normalize_space_xpath("span", "Training Sessions")
    MENU_EMPLOYEE_BUTTON = CommonLocators._normalize_space_xpath("span", "Employees")
    MENU_RECRUITMENT_ATS_BUTTON = CommonLocators._normalize_space_xpath("span", "Recruitment (ATS)")
    MENU_CORE_HR_BUTTON = CommonLocators._normalize_space_xpath("a", "Core HR")
    MENU_DEPARMENT_BUTTON = CommonLocators._normalize_space_xpath("a", "Department")
    MENU_DESIGNATION_BUTTON = CommonLocators._normalize_space_xpath("a", "Designation")
    MENU_POLICIES_BUTTON = CommonLocators._normalize_space_xpath("a", "Policies")
    MENU_MAKE_ANNOUNCEMENT_BUTTON = CommonLocators._normalize_space_xpath("a", "Make Announcement")
    MENU_ORGANIZATION_CHART_BUTTON = CommonLocators._normalize_space_xpath("a", "Organization Chart")
    MENU_FINANCE_BUTTON = CommonLocators._normalize_space_xpath("span", "Finance")
    MENU_PERFORMANCE_PMS_BUTTON = CommonLocators._normalize_space_xpath("a", "Performance (PMS)")
    MENU_KPI_INDICATOR_BUTTON = CommonLocators._normalize_space_xpath("a", "KPI (Indicator)")
    MENU_KPA_APPRAISAL_BUTTON = CommonLocators._normalize_space_xpath("a", "KPA (Appraisal)")
    MENU_CAMPETENCIES_BUTTON = CommonLocators._normalize_space_xpath("a", "Competencies")
    MENU_TRACK_GOALS_OKRS_BUTTON = CommonLocators._normalize_space_xpath("a", "Track Goals (OKRs)")
    MENU_GOAL_TYPE_BUTTON = CommonLocators._normalize_space_xpath("a", "Goal Type")
    MENU_GOALS_CALENDAR_BUTTON = CommonLocators._normalize_space_xpath("a", "Goals Calendar")
    MENU_INVENTORY_CONTOL_BUTTON = CommonLocators._normalize_space_xpath("span", "Inventory Control")
    MENU_WAREHOUSES_BUTTON = CommonLocators._normalize_space_xpath("a", "Warehouses")
    MENU_PRODUCTS_BUTTON = "//a[@href='#!'][normalize-space()='Products']"
    MENU_SUPPLIERS_BUTTON = CommonLocators._normalize_space_xpath("a", "Suppliers")
    MENU_PURCHASES_BUTTON = CommonLocators._normalize_space_xpath("a", "Purchases")
    MENU_SALES_ORDER_BUTTON = CommonLocators._normalize_space_xpath("a", "Sales Order")
    MENU_MANAGE_CLIENTS_BUTTON = CommonLocators._normalize_space_xpath("span", "Manage Clients")
    MENU_LEADS_BUTTON = CommonLocators._normalize_space_xpath("span", "Leads")
    MENU_INVOICES_BUTTON = CommonLocators._normalize_space_xpath("span", "Invoices")
    MENU_ESTIMATES_BUTTON = CommonLocators._normalize_space_xpath("span", "Estimates")
    MENU_DISCIPLINARY_CASES_BUTTON = CommonLocators._normalize_space_xpath("span", "Disciplinary Cases")
