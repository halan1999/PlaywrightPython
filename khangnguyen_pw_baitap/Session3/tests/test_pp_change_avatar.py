from playwright.sync_api import Page, expect
import re, time

def test_change_avatar(page: Page):
     # Access the Customer portal
     page.goto("https://apollo-k8s.parcelperform.com/login")

     # Login
     page.locator('//input[@name="email" and @type="email"]').fill('artemis.test01z@gmail.com')
     page.locator('//input[@placeholder="Password" and @type="password"]').fill('Artemis.test01z@pp.com')
     page.locator('//button[@type="submit" and normalize-space()="Log in"]').click()

     # Choose merchant
     dropdown_field = page.locator('//input[@type="text" and @placeholder="Select account"]')
     dropdown_field.click()
     page.locator('//div[contains(@class, "dropdown-content")]/descendant::li[text()="Trọn Đời Bên Em"]').click()
     page.locator('//button[@type="submit" and text()="Continue"]').click()

     # expect(page.locator('//ol[contains(@class,"ppDisFlex ppContentPos")]/descendant::span[normalize-space()="Home"]')).to_be_visible()

     # Click user profile on home page
     page.locator('//div[@class="ppClickable dropdown"]/descendant::strong[contains(@class,"pp-text-primary-sup")]').click()
     page.locator('//button[@type="button"]/child::div[contains(@class,"pp-profile")]').click()
     
     # Upload avatar
     page.locator('#customInputButton').set_input_files("image123.jpg")
     page.locator('//button[contains(@class,"BaseButton") and text()="Save"]').click()




     




     