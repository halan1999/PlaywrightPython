from playwright.sync_api import Page, expect

url: str = "https://crm.anhtester.com/admin/authentication"

def get_menu_item_locator(menu_name: str, index_item = None) -> str:
    base = f"//ul[@id='side-menu']/descendant::span[contains(text(), '{menu_name}')]"
    if index_item is not None:
        base = f"({base})[{index_item}]"
    return base

def get_sub_menu_item_locator(sub_menu_name: str) -> str:
    return f"//span[@class='sub-menu-text' and normalize-space(text())='{sub_menu_name}']"

def input_xpath_by_type (type: str) -> str:
    return f"//input[@type='{type}']"

def button_xpath_by_type (type: str) -> str:
    return f"//button[@type='{type}']"

def xpath_widget_dashboard (value_attribute: str, attribute: str, text: str) -> str:
    return f"//div[@id='{value_attribute}']//{attribute}[normalize-space(text())='{text}']"
    
def xpath_widget_finance_dashboard (index: int, atribute: str, text: str) -> str:
    return f"//div[@id='widget-finance_overview']/descendant::div[@class='row'][{index}]/descendant::{atribute}[contains(normalize-space(), '{text}')]"

def test_locators_css_id(page: Page):
    #----------------------
    # LOGIN
    #----------------------
    page.goto(url)
    page.locator(input_xpath_by_type("email")).fill("admin@example.com")
    page.locator(input_xpath_by_type("password")).fill("123456")
    page.locator(button_xpath_by_type("submit")).click()

    #----------------------
    # MENU LOCATORS
    #----------------------
    #click dashboard menu
    page.locator(get_menu_item_locator("Dashboard")).click()
    # dashboard items
    # widgets top
    invoices_awaiting_payment_widget_top = page.locator(xpath_widget_dashboard("widget-top_stats", "span", "Invoices Awaiting Payment"))
    converted_leads_widget_top = page.locator(xpath_widget_dashboard("widget-top_stats", "span", "Converted Leads"))
    projects_in_progress_widget_top = page.locator(xpath_widget_dashboard("widget-top_stats", "span", "Projects In Progress"))
    tasks_not_finished_widget_top = page.locator(xpath_widget_dashboard("widget-top_stats", "span", "Tasks Not Finished"))
    # widgets finance
    invoice_status_draft_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Draft"))
    invoice_status_not_sent_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Not Sent"))
    invoice_status_unpaid_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Unpaid"))
    invoice_status_partially_paid_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Partially Paid"))
    invoice_status_overdue_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Overdue"))
    invoice_status_paid_widget_finance = page.locator(xpath_widget_finance_dashboard(1, "a", "Paid"))
    estimate_status_draft_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Draft"))
    estimate_status_not_sent_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Not Sent"))
    estimate_status_sent_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Sent"))
    estimate_status_expired_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Expired"))
    estimate_status_declined_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Declined"))
    estimate_status_accepted_widget_finance = page.locator(xpath_widget_finance_dashboard(2, "a", "Accepted"))
    proposal_status_draft_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Draft"))
    proposal_status_sent_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Sent"))
    proposal_status_open_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Open"))
    proposal_status_revised_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Revised"))
    proposal_status_declined_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Declined"))
    proposal_status_accepted_widget_finance = page.locator(xpath_widget_finance_dashboard(3, "a", "Accepted"))
    # widget invoice overview
    outstanding_invoices_widget_finance = page.locator(xpath_widget_dashboard("invoices_total", "dt", "Outstanding Invoices"))
    paid_due_invoices_widget_finance = page.locator(xpath_widget_dashboard("invoices_total", "dt", "Past Due Invoices"))
    paid_incoies_widget_finance = page.locator(xpath_widget_dashboard("invoices_total", "dt", "Paid Invoices"))
    
    # customers menu
    page.locator(get_menu_item_locator("Customers")).click()
    # sale menu
    page.locator(get_menu_item_locator("Sales", 1)).click()
    # submenu sale: proposal menu
    page.locator(get_sub_menu_item_locator("Proposals")).wait_for(state="visible")
    page.locator(get_sub_menu_item_locator("Proposals")).click()
    # submenu sale: estimate menu
    page.locator(get_sub_menu_item_locator("Estimates")).click()
    # submenu sale: invoices menu
    page.locator(get_sub_menu_item_locator("Invoices")).click()
    # submenu sale: payments menu
    page.locator(get_sub_menu_item_locator("Payments")).click()
    # submenu sale: credit notes menu
    page.locator(get_sub_menu_item_locator("Credit Notes")).click()
    # submenu sale: items menu
    page.locator(get_sub_menu_item_locator("Items")).click()
    # subscriptions menu
    page.locator(get_menu_item_locator("Subscriptions")).click()
    # expenses menu
    page.locator(get_menu_item_locator("Expenses", 1)).click()
    # contracts menu
    page.locator(get_menu_item_locator("Contracts")).click()
    # projects menu
    page.locator(get_menu_item_locator("Projects")).click()
    # tasks menu
    page.locator(get_menu_item_locator("Tasks")).click()
    # support menu
    page.locator(get_menu_item_locator("Support")).click()
    # leads menu    
    page.locator(get_menu_item_locator("Leads", 1)).click()
    # estimate request menu
    page.locator(get_menu_item_locator("Estimate Request")).click()
    #knowledge base menu
    page.locator(get_menu_item_locator("Knowledge Base")).click()
    # ultimate menu 
    page.locator(get_menu_item_locator("Utilities")).click()
    # submenu ultimate: media menu
    page.locator(get_sub_menu_item_locator("Media")).click()
    # submenu ultimate: bulk PDF Export menu
    page.locator(get_sub_menu_item_locator("Bulk PDF Export")).click()
    # submenu ultimate: calendar menu
    page.locator(get_sub_menu_item_locator("Calendar")).click()
    # reports menu
    page.locator(get_menu_item_locator("Reports")).click()
    # submenu reports: sales menu
    page.locator(get_sub_menu_item_locator("Sales")).click()
    # submenu reports: expenses menu
    page.locator(get_sub_menu_item_locator("Expenses")).click()
    # submenu reports: expenses vs income menu
    page.locator(get_sub_menu_item_locator("Expenses vs Income")).click()
    # submenu reports: leads menu
    page.locator(get_sub_menu_item_locator("Leads")).click()
    # submenu reports: timesheets overview menu
    page.locator(get_sub_menu_item_locator("Timesheets overview")).click()
    # submenu reports: KB articles menu
    page.locator(get_sub_menu_item_locator("KB Articles")).click()
    #----------------------
    # DASHBOARD LOCATORS
    #----------------------