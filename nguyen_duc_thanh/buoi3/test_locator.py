from playwright.sync_api import Page, expect
import time,re

def test_locator(page: Page):
    page.goto("https://crm.anhtester.com/admin/")
    page.fill("//input[@id='email']","admin@example.com")
    page.fill("//input[@id='password']","123456")
    page.click("//button[@type='submit']")
    # Dashboard
    Dashboard = page.locator("//span[normalize-space()='Dashboard']")
    Invoices_Awaiting_Payment = page.locator("//span[normalize-space()='Invoices Awaiting Payment']")
    Invoices_Awaiting_Payment_progressbar = page.locator("//div[@class='quick-stats-invoices col-xs-12 col-md-6 col-sm-6 col-lg-3 tw-mb-2 sm:tw-mb-0']//div[@role='progressbar']")
    Converted_Leads = page.locator("//span[normalize-space()='Converted Leads']")
    Converted_Leads_progressbar = page.locator("//div[@class='quick-stats-leads col-xs-12 col-md-6 col-sm-6 col-lg-3 tw-mb-2 sm:tw-mb-0']//div[@role='progressbar']")
    Dashboard_Options = page.locator("//div[@class='screen-options-btn']")
    View_All = page.locator("//a[@class='tw-text-sm tw-mb-0']")
    New_To_Do = page.locator("//a[@class='tw-text-sm tw-mb-0 tw-pl-2']")
    Lead_Overview_chart = page.locator("//canvas[@id='leads_status_stats']")
    Statistics_by_Project_Status_chart = page.locator("//canvas[@id='projects_status_stats']")
    Export_button = page.locator("//span[normalize-space()='Export']")

    # Customers
    Customers = page.locator("//span[normalize-space()='Customers']")
    New_Customers_btn = page.locator("//a[@class='btn btn-primary mright5 test pull-left display-block']")
    Import_Customters_btn = page.locator("//a[@class='btn btn-primary pull-left display-block mright5 hidden-xs']")
    Contact_btn = page.locator("//a[@class='btn btn-default pull-left display-block mright5']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    Search_Field = page.locator("//input[@class='form-control input-sm']")
    Active_button = page.locator("//div[@class='onoffswitch']")
    Page_Dropdown = page.locator("//select[@name='clients_length']")
    ID_Sorting_Arrow = page.locator("//th[@id='th-number']")
    Delete = page.locator("//tr[@class='has-row-options odd']//div[@class='row-options']//a[contains(@class, '_delete')]")
    View = page.locator("//tr[@class='has-row-options odd']//div[@class='row-options']//a[normalize-space(text())='View']")

    # Subscriptions
    Subscriptions = page.locator("//span[normalize-space()='Subscriptions']")    
    New_Subscriptions =  page.locator("//a[@class='btn btn-primary pull-left display-block']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    Search_Field = page.locator("//input[@class='form-control input-sm']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    Not_Subcribed_Number = page.locator("//div[@class='tw-grid tw-grid-cols-2 md:tw-grid-cols-3 lg:tw-grid-cols-8 tw-gap-2 tw-mt-2 sm:tw-mt-4']//div[2]//span[1]")
    # Sales
    Sales = page.locator("//li[@class='menu-item-sales']//span[@class='menu-text']")
    Proposals = page.locator("//span[normalize-space()='Proposals']")
    New_Proposals = page.locator("//a[@class='btn btn-primary pull-left display-block new-proposal-btn']")
    Toggle_Tabel = page.locator("//i[@class='fa fa-angle-double-left']")
    Reload = page.locator("//i[@class='fa fa-refresh']")
    Estimates = page.locator("//span[normalize-space()='Estimates']")
    View_Quick_Stats = page.locator("//i[@class='fa fa-bar-chart']")
    Switch_To_Pipline = page.locator("//i[@class='fa-solid fa-grip-vertical']")
    Invoices = page.locator("//span[normalize-space()='Invoices']")
    Payments = page.locator("//span[normalize-space()='Payments']")
    Items = page.locator("//span[normalize-space()='Items']")

    #Expenses
    Expenses = page.locator("//span[@class='menu-text'][normalize-space()='Expenses']")
    Record_Expense = page.locator("//a[normalize-space()='Record Expense']")
    Import_Expenses = page.locator("//a[@class='btn btn-primary mleft5']")
    Toggle_Table = page.locator("//i[@class='fa fa-angle-double-left']")
    View_Quick_Stats = page.locator("//i[@class='fa fa-bar-chart']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    
    # Contracts
    Contracts = page.locator("//span[normalize-space()='Contracts']")
    New_Contract = page.locator("//a[@class='btn btn-primary pull-left display-block tw-mb-2 sm:tw-mb-4']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    Contracts_by_Type = page.locator("//canvas[@id='contracts-by-type-chart']")
    Contracts_Value_by_Type = page.locator("//canvas[@id='contracts-value-by-type-chart']")
    Export_button = page.locator("//span[normalize-space()='Export']")
   
    # Projects
    Projects = page.locator("//span[normalize-space()='Projects']")
    New_Project = page.locator("//a[@class='btn btn-primary pull-left display-block mright5']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    In_Progress_Status = page.locator("//span[contains(@class, 'project-status') and normalize-space()='In Progress']")
    hieu_tag = page.locator("//div[@class='tags-labels']//span[@class='tag' and normalize-space()='hieu']")
    Not_Started = page.locator("//span[contains(@class, 'project-status') and normalize-space()='Not Started']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    
    #Tasks
    Tasks = page.locator("//span[normalize-space()='Tasks']")
    New_Task = page.locator("//a[@class='btn btn-primary pull-left new']")
    Task_Overview = page.locator("//a[@class='btn btn-success pull-right mright5']")
    Staus_Dropdown = page.locator("//span[@data-original-title='Change Status']//i[@class='fa-solid fa-chevron-down tw-opacity-70']")
    Priority_Dropdown = page.locator("//span[@data-original-title='Priority']//i[@class='fa-solid fa-chevron-down tw-opacity-70']")
    Export_button = page.locator("//span[normalize-space()='Export']")

    #Support
    Support = page.locator("//span[normalize-space()='Support']")
    New_Ticket = page.locator("//a[@class='btn btn-primary pull-left display-block mright5']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    Reload = page.locator("//i[@class='fa fa-refresh']")
    Weekly_Stats = page.locator("//i[@class='fa fa-bar-chart']")
    
    #Leads
    Lead = page.locator("//span[@class='menu-text'][normalize-space()='Leads']")
    New_Lead = page.locator("//a[@class='btn btn-primary mright5 pull-left display-block']")
    Filter = page.locator("//i[@class='fa fa-filter']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    Reload = page.locator("//i[@class='fa fa-refresh']")
    Search_Field = page.locator("//input[@class='form-control input-sm']")

    #Estimate Request
    Estimate_Request = page.locator("//span[normalize-space()='Estimate Request']")
    New_Form = page.locator("//a[@class='btn btn-primary']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    Reload = page.locator("//i[@class='fa fa-refresh']")
    Search_Field = page.locator("//input[@class='form-control input-sm']")

    #Knowledge Base
    Knowledge_Base = page.locator("//span[normalize-space()='Knowledge Base']")
    New_Article = page.locator("//a[@class='btn btn-primary mright5']")
    Export_button = page.locator("//span[normalize-space()='Export']")
    Reload = page.locator("//i[@class='fa fa-refresh']")
    Search_Field = page.locator("//input[@class='form-control input-sm']")
    Group_button = page.locator("//a[@class='btn btn-default mright5']") 
    #Utilites
    Utilites = page.locator("//span[normalize-space()='Utilities']")
    Media = page.locator("//span[normalize-space()='Media']")
    Media_Screen = page.locator("//div[@id='elfinder']")

    Bulk_PDF_ExportUtilites = page.locator("//span[normalize-space()='Bulk PDF Export']")
    Select_Type = page.locator("//div[@class='col-md-6 col-md-offset-3']//form")
    From_Date = page.locator("//div[@class='xdsoft_datepicker active']")
    To_Date = page.locator("//input[@id='date-to']")
    Include_Tag = page.locator("//input[@id='tag']")
    Export = page.locator("//button[@type='submit']")

    Calendar =  page.locator("//span[normalize-space()='Calendar']")
    Today_button =  page.locator("//button[normalize-space()='today']")
    Left_Arrow =  page.locator("//span[@class='fc-icon fc-icon-chevron-left']")
    Right_Arrow =  page.locator("//span[@class='fc-icon fc-icon-chevron-right']")
    Month =  page.locator("//button[normalize-space()='month']")
    Week =  page.locator("//button[normalize-space()='week']")
    Day =  page.locator("//button[normalize-space()='day']")
    Filter_by = page.locator("//button[normalize-space()='filter by']")

    #Report
    Report = page.locator("//span[normalize-space()='Reports']")
    Sales = page.locator("//span[@class='sub-menu-text'][normalize-space()='Sales']")
    Expenses = page.locator("//span[@class='sub-menu-text'][normalize-space()='Expenses']")
    Expenses_vs_Income = page.locator("//span[normalize-space()='Expenses vs Income']")
    Leads = page.locator("//span[@class='sub-menu-text'][normalize-space()='Leads']")
    Timesheets_overview = page.locator("//span[normalize-space()='Timesheets overview']")
    KB_Articles = page.locator("//span[normalize-space()='KB Articles']")





