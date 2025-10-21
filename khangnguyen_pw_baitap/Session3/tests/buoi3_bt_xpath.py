from playwright.sync_api import Page, expect
import re

def test_xpath_locating(page: Page):
     page.goto("https://crm.anhtester.com/admin")

     # Login form
     email_field = page.locator('//input[@id="email"]')
     password_field = page.locator('//input[@id="password"]')
     login_button = page.locator('//button[normalize-space()="Login"]')


     email_field.fill('admin@example.com')
     password_field.fill('123456')
     login_button.click()

     # Menu Items
     dashboard_menuitem = page.locator('//li[contains(@class,"menu-item-dashboard")]')
     customers_menuitem = page.locator('//li[contains(@class,"menu-item-customers")]')
     sales_menuitem = page.locator('//li[contains(@class,"menu-item-sales")]')
     subscriptions_menuitem = page.locator('//li[contains(@class,"menu-item-subscriptions")]')
     expenses_menuitem = page.locator('//li[contains(@class,"menu-item-expenses")]')
     contracts_menuitem = page.locator('//li[contains(@class,"menu-item-contracts")]')
     projects_menuitem = page.locator('//li[contains(@class,"menu-item-projects")]')
     tasks_menuitem = page.locator('//li[contains(@class,"menu-item-tasks")]')
     support_menuitem = page.locator('//li[contains(@class,"menu-item-support")]')
     leads_menuitem = page.locator('//li[contains(@class,"menu-item-leads")]')
     estimate_request_menuitem = page.locator('//li[contains(@class,"menu-item-estimate_request")]')
     knowledge_base_menuitem = page.locator('//li[contains(@class,"menu-item-knowledge-base")]')
     utilities_menuitem = page.locator('//li[contains(@class,"menu-item-utilities")]')
     reports_menuitem = page.locator('//li[contains(@class,"menu-item-reports")]')


     # Toolbars
     expand_button_icon = page.locator('//div[@class="hide-menu tw-ml-1"]')
     search_field = page.locator('//input[@id="search_input" or @placeholder="Search..."]')
     quick_create_button_icon = page.locator('//span[contains(@class,"tw-rounded-ful")]')
     share_button_cion = page.locator('//a[@data-original-title="Share documents, ideas.."]')
     to_do_button_icon = page.locator('//a[@data-original-title="Todo items"]')
     user_profile_button_icon = page.locator('//img[contains(@class,"staff-profile-image-small")]')
     my_time_sheet_button_icon = page.locator('//a[@id="top-timers"]')
     notification_button_icon = page.locator('//a[contains(@class,"notifications-icon")]')
     dashboard_options_button = page.locator('//div[normalize-space()="Dashboard Options"]')

     # Invoices Awating Payment
     invoice_awaiting_payment_text = page.locator('//span[normalize-space()="Invoices Awaiting Payment"]')
     invoice_awaiting_payment_box = page.locator('//span[normalize-space()="Invoices Awaiting Payment"]/ancestor::div[contains(@class,"quick-stats-invoices")]')
     invoice_awaiting_payment_progress_bar = page.locator('//div[contains(@class,"quick-stats-invoices")]/descendant::div[contains(@role,"progressbar")]')

     
     # Converted Leads
     converted_leads_text = page.locator('//span[normalize-space()="Converted Leads"]')
     converted_leads_box = page.locator('//div[@class="top_stats_wrapper"]/parent::div[contains(@class,"quick-stats-leads")]')
     converted_leads_progress_bar = page.locator('//div[contains(@class,"quick-stats-leads")]/descendant::div[contains(@role,"progressbar")]')

     # Projects In Progress
     projects_in_progress_text = page.locator('//span[normalize-space()="Projects In Progress"]')
     projects_in_progress_box = page.locator('//div[@class="top_stats_wrapper"]/parent::div[contains(@class,"quick-stats-projects")]')
     projects_in_progress_progress_bar = page.locator('//div[contains(@class,"quick-stats-projects")]/descendant::div[contains(@role,"progressbar")]')

     # Tasks Not Finished
     tasks_not_finished_text = page.locator('//span[normalize-space()="Tasks Not Finished"]')
     projects_in_progress_box = page.locator('//div[@class="top_stats_wrapper"]/parent::div[contains(@class,"quick-stats-tasks")]')
     projects_in_progress_progress_bar = page.locator('//div[contains(@class,"quick-stats-tasks")]/descendant::div[contains(@role,"progressbar")]')

     # Overview (Invoice, Estimate, Proposal)
     overview_panel = page.locator('//div[@id="widget-finance_overview"]')
     invoice_overview_text = page.locator('//span[normalize-space()="Invoice overview"]')
     estimate_overview_text = page.locator('//span[normalize-space()="Estimate overview"]')
     proposal_overview_text = page.locator('//span[normalize-space()="Proposal overview"]')

     invoice_overview_draft_status = page.locator('//div[@id="widget-finance_overview"]//a[contains(@href, "/invoices/list_invoices") and contains(normalize-space(.), "Draft") ]')
     estimate_overview_draft_status = page.locator('//div[@id="widget-finance_overview"]//a[contains(@href, "/estimates/list_estimates") and contains(normalize-space(.), "Draft") ]')
     proposal_overivew_draft_status = page.locator('//div[@id="widget-finance_overview"]//a[contains(@href, "/proposals/list_proposals") and contains(normalize-space(.), "Draft") ]')

     # My To Do Items
     view_all_button_text = page.locator('//div[@id="widget-todos"]/descendant::a[normalize-space()="View All"]')
     new_to_do_button_text = page.locator('//div[@id="widget-todos"]/descendant::a[normalize-space()="New To Do"]')











