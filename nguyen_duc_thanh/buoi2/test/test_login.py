from playwright.sync_api import Page, expect
import time,re

       
def test_login_with_standard_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("//input[@id='user-name']","standard_user")
    page.fill("//input[@id='password']","secret_sauce")
    page.click("//input[@id='login-button']")
    expect(page.get_by_text("Products")).to_be_visible()
    items = page.locator("//div[@data-test='inventory-item']")
    names = items.all_text_contents()
    for name in names:
        print(f"{name}\n")
    expect(items).to_have_count(6)

def test_login_with_locked_out_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()

def test_login_with_problem_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("problem_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_with_performance_glitch_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("//input[@id='user-name']","performance_glitch_user")
    page.fill("//input[@id='password']","secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_with_error_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("problem_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.click("//input[@id='login-button']")
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_with_visual_user(page : Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("visual_user")
    page.fill("//input[@id='password']","secret_sauce")
    page.click("//input[@id='login-button']")
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_failed(page :Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.fill("//input[@id='password']","secret_sauces")
    page.click("//input[@id='login-button']")
    expect(page.locator("//h3[@data-test='error']")).to_contain_text("Username and password do not match any user in this service")
    



 