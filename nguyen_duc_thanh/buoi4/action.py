from playwright.sync_api import Page,expect
import time,re,pytest
from datetime import datetime

def test_department(page:Page):  
    url = 'https://hrm.anhtester.com/erp/login'
    username = 'admin_example'
    password = '123456'

    #Login
    page.goto(url)
    page.locator("//input[@id='iusername']").fill(username)
    page.locator("//input[@id='ipassword']").fill(password)
    page.locator("//span[@class='ladda-label']").click()
    expect(page.get_by_text("Welcome admin_example hello")).to_be_visible()
    page.locator("//a[normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()
    
    # Add Name
    timestamp = datetime.now().strftime("%H%M%S") 
    uni_name = 'thanh' + timestamp
    name = page.locator("//input[@placeholder='Name']")
    name.fill(uni_name)
    expect (name).to_have_value(uni_name)
    page.locator("//div[@class='card-footer text-right']//button[@type='submit']").click()
    toast_message = page.locator("//div[@class='toast-message']")
    expect (toast_message).to_contain_text("Department added.") 
    time.sleep(3)

    #Search
    search = page.locator("//input[@type='search']")
    search.fill(uni_name)
    expect (search).to_have_value(uni_name)
    result = page.locator("(//tr[@role='row']//td[@class='sorting_1'])[1]")
    expect (result).to_contain_text(uni_name)
    time.sleep(3)
    #Edit

    edit_btn = page.locator("//button[@class = 'btn icon-btn btn-sm btn-light-primary waves-effect waves-light']")
    edit_btn.click()
    edit_name = page.locator(f"//div[@class='form-group']//input[@class='form-control' and normalize-space(@value)='{uni_name}']")
    edit_name.fill(uni_name)
    update = page.locator("//button[@class='btn btn-primary ladda-button' and normalize-space() = 'Update']")
    update.click()
    expect (toast_message).to_contain_text("Department updated.") 
    time.sleep(3)
    
    #Deleted
    search.fill(uni_name)
    delete_btn = page.locator(f"//td[normalize-space()='{uni_name}']//i[@class='feather icon-trash-2']")
    delete_btn.click()
    confirm = page.locator("//button[@class='btn btn-primary ladda-button' and normalize-space() = 'Confirm']")
    confirm.click()
    expect (toast_message).to_contain_text("Department deleted.")

    


    
