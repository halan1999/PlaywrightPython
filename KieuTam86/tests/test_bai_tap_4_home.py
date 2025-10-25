from playwright.sync_api import Playwright, Page, expect
import re, time

def test_Dropdown_list(page:Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown_Position = page.locator("#dropdown")

    #cách 1
    # dropdown_Position.select_option("2")
    #cách 2
    dropdown_Position.select_option(label="Option 2")

    expect(page.locator("option:checked")).to_have_text("Option 2")
    print("Đã chọn đúng option 2")

    page.close()

def test_Hovers(page:Page):
    page.goto("https://the-internet.herokuapp.com/hovers")

    user3_position = page.locator("div.figure:nth-child(5)")
    user3_position.hover()
    # hoặc sử dụng
    # page.locator("div.figure").nth(2).hover()
    expect(page.get_by_text("name: user3")).to_be_visible()

    page.close()

def test_Upload_file(page:Page):
    #Open brownser
    page.goto("https://the-internet.herokuapp.com/upload")

    # Create empty file
    with open("my_test_file.txt", "w") as f:
        f.write("")
    # Act
        page.set_input_files("#file-upload", "my_test_file.txt")
        page.click("#file-submit")
    # Assert
    expect(page.locator("#uploaded-files")).to_contain_text("my_test_file.txt")

    print("Upload file successfully!")
    page.close()    

