from playwright.sync_api import Page, expect

def test_new_tab_windows(page:Page):
    base_url="https://the-internet.herokuapp.com/windows"
    page.goto(base_url)
    heading=page.locator('h3')
    expect(heading).to_have_text("Opening a new window")
    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    new_page=popup_info.value
    new_page.wait_for_load_state()
    assert "/windows/new" in new_page.url
    new_heading=new_page.locator('h3')
    expect(new_heading).to_have_text("New Window")
    new_page.close()

    