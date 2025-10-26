from playwright.sync_api import Page,expect
import time,re

def test_core_hr(page :Page):
    page.goto("https://hrm.anhtester.com/erp/login")
    page.locator("//input[@id='iusername']").fill("admin_example")
    page.locator("//input[@id='ipassword']").fill("123456")
    page.locator("//i[@class='fas fa-user-lock d-blockd']").click()
    expect(page.get_by_text("Welcome admin_example hello")).to_be_visible()
    
    # Core HR
    page.locator("//a[normalize-space()='Core HR']")
    #Department
    page.locator("//a   ")
    #Name Field
    page.locator("//input[@class='form-control']")

    #Save btn
    page.locator("//button[@class='btn btn-primary ladda-button']")

    #Row 1 - Result
    page.locator("(//tr[@class='odd'])[1]")

    #Edit Row1
    page.locator("(//button[@class='btn icon-btn btn-sm btn-light-primary waves-effect waves-light'])[1]")

    #Delete Row1
    page.locator("(//button[@class='btn icon-btn btn-sm btn-light-danger waves-effect waves-light delete'])[1]")

    #Department icon tab
    page.locator("//a[@class='mb-3 nav-link']//span[@class='sw-icon feather icon-align-justify']")

    #Designation icon tab
    page.locator("//a[@class='mb-3 nav-link']//span[@class='sw-icon feather icon-list']")

    #Department dropdown
    page.locator("//span[@class='select2-selection__rendered']")

    #Designation Name textfield
    page.locator("//input[@class='form-control']")

    #Description textfield
    page.locator("//textarea[@placeholder='Description']")

    #Save btn
    page.locator("//button[contains(@class,'btn-primary') and contains(.,'Save')]")

    #Row 1 - Result
    page.locator("(//tr[@class='odd'])[1]")

    #Search field
    page.locator("//input[@type='search']")

    #Result Dropdown
    page.locator("//select[@name='xin_table_length']")

    #Announcements icon tab
    page.locator("//a[@class='mb-3 nav-link']//span[@class='sw-icon feather icon-speaker']")

    #Addnew button
    page.locator("//a[@class='collapsed btn waves-effect waves-light btn-primary btn-sm m-0']")

    #Search field
    page.locator("//input[@class='form-control form-control-sm']")

    #Title
    page.locator("//input[@placeholder='Title']")

    #Start Date
    page.locator("//input[@class='form-control date'][@name='start_date']")

    #End Date
    page.locator("//input[@class='form-control date'][@name='end_date']")
    
    #Department dropdown
    page.locator("//ul[@class='select2-selection__rendered']")

    #Summary
    page.locator("//input[@id='summary'")

    #Policies icon tab
    page.locator("//a[@class='mb-3 nav-link']//span[@class='sw-icon feather icon-pocket']")
   
    #title
    page.locator("//input[@placeholder='Title']")

    #Description
    page.locator("//textarea[@id='description']")

    #Attachment
    page.locator("//input[@id='attachment']")

    #Save btn
    page.locator("//button[contains(@class,'btn-primary') and contains(.,'Save')]")




