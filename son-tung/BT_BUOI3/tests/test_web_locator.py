from playwright.sync_api import Page

def test_web_locator(page : Page):
    page.goto("https://crm.anhtester.com/admin")

    page.locator("//input[@name='email']").fill("admin@example.com")
    page.locator("//input[@name='password']").fill("123456")

    page.locator("//button[@type='submit']").click()

    ### MENU SIDEBAR:
    menu = ["Dashboard", "Customers", "Sales", "Subscriptions", "Expenses", "Contracts", "Projects", "Tasks", "Support",
            "Leads", "Estimate Request", "Knowledge Base", "Utilities", "Reports", "Bulk PDF Export", "Calendar", "Media"]
    for i in menu:
        page.locator(f"//span[normalize-space()='{i}']")

    subMenuSales = ["Proposals", "Estimates", "Invoices", "Payments", "Credit Notes", "Items"]
    for i in subMenuSales:
        page.locator(f"//span[normalize-space()='Sales']//following::span[normalize-space()='{i}']")

    subMenuReport = ["Sales", "Expenses", "Expenses vs Income", "Timesheets overview", "KB Articles"]
    for i in subMenuReport:
        page.locator(f"//span[normalize-space()='Reports']//following::span[normalize-space()='{i}']")


    ### HEADER
    # Input search
    page.locator("//input[@id='search_input']")
    # Button search
    page.locator("//div[@id='top_search_button']//button")
    # Button Quick Create
    page.locator("//li[@data-original-title='Quick Create']")
    # Button Share
    page.locator("//a[@class='open_newsfeed desktop']")
    # Button Todo Items
    page.locator("//li[@class='icon header-todo']//a")
    # Avatar
    page.locator("//li[@class='icon header-user-profile']//img")
    # Button Timesheets
    page.locator("//li[@data-title='My Timesheets']")
    # Button Notifications
    page.locator("//li[@data-original-title='Notifications']")
    # Button Dashboard Options
    page.locator("//div[@class='screen-options-btn']")


    ### WIDGET RELATIVE
    # Label of wrapper: Use to verify label text visible
    label = ["invoices", "leads", "projects", "tasks"]
    for i in label:
        page.locator(f"//div[contains(@class,'quick-stats-{i}')]//span[@class='tw-truncate']")
    # Detail of wrapper: The detail of statistics of wrapper
    for i in label:
        page.locator(f"//div[contains(@class,'quick-stats-{i}')]//span[@class='tw-truncate']//following::span[1]")
    # Progressbar: Use to get value visible in UI
    for i in label:
        page.locator(f"//div[contains(@class,'quick-stats-{i}')]//div[@role='progressbar']")

    ### WIDGET FINANCE
    # Label Overview: Use to verify label text visible
    page.locator("(//div[@class='finance-summary']//span)[1]")
    page.locator("(//div[@class='finance-summary']//span)[8]")
    # Detail: The detail of statistics of overview
    for i in range(1, 18):
        page.locator(f"//span[normalize-space()='Invoice overview']//following::span[@class='_total bold'][{i}]")
        page.locator(f"//span[normalize-space()='Invoice overview']//following::span[@class='_total bold'][{i}]/parent::a")


    ### WIDGET TODO
    # Label My Todo Items: Use to verify label text visible
    page.locator("//div[@id='widget-todos']//p")
    # Button View All
    page.locator("//div[@id='widget-todos']//a[normalize-space()='View All']")
    # Button New Todo
    page.locator("//div[@id='widget-todos']//a[normalize-space()='New To Do']")
    # Title Latest Todo
    page.locator("//div[@id='widget-todos']//p//following::h4[1]")
    page.locator("//div[@id='widget-todos']//h4[contains(@class, 'text-warning')]")
    page.locator("//div[@id='widget-todos']//p//following::h4[2]")
    page.locator("//div[@id='widget-todos']//h4[contains(@class, 'text-success')]")

    # Checkbox List Todo
    for i in range(1, 4):
        page.locator(f"//ul[1]//li[{i}]//input[@type='checkbox']")
    for i in range(1, 2):
        page.locator(f"//ul[2]//li[{i}]//input[@type='checkbox']")
    # Button edit Todo
    for i in range(1, 4):
        page.locator(f"//div[@id='widget-todos']//ul[1]//li[{i}]//a[2]//i")
    for i in range(1, 2):
        page.locator(f"//div[@id='widget-todos']//ul[2]//li[{i}]//a[2]//i")
    # Button delete Todo
    for i in range(1, 4):
        page.locator(f"//div[@id='widget-todos']//ul[1]//li[{i}]//a[1]")
    for i in range(1, 2):
        page.locator(f"//div[@id='widget-todos']//ul[2]//li[{i}]//a[1]")


    ### WIDGET LEADS CHART
    # Label: Use to verify label text visible
    page.locator("//div[@data-name='Leads Chart']//p//span")
    # Canvas: Use to verify canvas visible
    page.locator("//div[@data-name='Leads Chart']//canvas")


    ### USER DATA WIDGET
    # Click button Task length
    page.locator("//div[@id='widget-user_data']//select[@name='tasks_length']").click()
    # Length options
    lstLength = ["10", "25", "50", "100", "-1"]
    for i in lstLength:
        page.locator(f"//div[@id='widget-user_data']//select[@name='tasks_length']//option[@value='{i}']")

    # Click button Export
    page.locator("//div[@id='widget-user_data']//button[@aria-controls='tasks']//span[normalize-space()='Export']").click()
    # Type of export file
    lstFileType = ["excel", "csv", "pdf", "print"]
    for i in lstFileType:
        page.locator(f"//div[@id='widget-user_data']//ul[@class='dropdown-menu']//li[contains(@class,'{i}')]")
    # Button Reload
    page.locator("//div[@id='widget-user_data']//button[@data-original-title='Reload']")

    # Input search
    page.locator("//div[@class='input-group']//input[@aria-controls='tasks']")

    ### WIDGET CALENDAR
    # Action with month calendar: next/previous
    page.locator("//div[@id='widget-calendar']//button[@aria-label='prev']")
    page.locator("//div[@id='widget-calendar']//button[@aria-label='next']")
    # Button Today: Use to choose date
    page.locator("//div[@id='widget-calendar']//button[normalize-space()='today']")
    # Today in grid calendar
    page.locator("//div[@id='calendar']//td[contains(@class,'today')]")
    # Button Expand
    page.locator("//div[@id='widget-calendar']//button[normalize-space()='expand']")
    # Label Month Year: Use to verify month year visible
    page.locator("//div[@id='widget-calendar']//h2")


    ### WIDGET PAYMENTS CHART
    # Label: Use to verify label text visible
    page.locator("//div[@id='widget-payments_chart']//span[contains(@class,'tw-text')]")
    # Canvas: Use to verify canvas visible
    page.locator("//canvas[@id='payment-statistics']")
    # Button Full Reports
    page.locator("//a[normalize-space()='Full Report']")
    # Button choose time mode
    page.locator("//span[@id='Payment-chart-name']").click()
    page.locator("//ul[@aria-labelledby='PaymentChartmode']//a[normalize-space()='Weekly']")
    page.locator("//ul[@aria-labelledby='PaymentChartmode']//a[normalize-space()='Monthly']")