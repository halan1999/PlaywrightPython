from playwright.sync_api import Page, expect
from pages.Multitab_demo.OrangeLoginPage import OrangeLoginPage
def test_orangehr_socicals(orange_login_page:OrangeLoginPage):
    login_page=orange_login_page
    page=login_page.page
    context=page.context
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Linked tab
    linkedin_icon= login_page.linkedin_icon()
    with context.expect_page() as page_info:
        linkedin_icon.click()
    linked_new_page=page_info.value
    linked_new_page.wait_for_load_state()
    assert "linkedin.com/company/orangehrm" in linked_new_page.url
    page.bring_to_front()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    facebook_icon=login_page.facebook_icon()
    #facebook tab
    with context.expect_page() as page_info:
         facebook_icon.click()
    facebook_new_page=page_info.value
    facebook_new_page.wait_for_load_state()
    assert "facebook.com/OrangeHRM/" in facebook_new_page.url
    page.bring_to_front()
    expect(page).to_have_url ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Twitter tab
    with context.expect_page() as page_info:
         twitter_icon=login_page.twitter_icon()
         twitter_icon.click()
    twitter_new_page=page_info.value
    twitter_new_page.wait_for_load_state()
    assert "x.com/orangehrm?lang=en" in twitter_new_page.url
    page.bring_to_front()
    expect(page).to_have_url ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Youtube tab
    with context.expect_page() as page_info:
         youtube_icon=login_page.youtube_icon()
         youtube_icon.click()
    youtube_new_page=page_info.value
    youtube_new_page.wait_for_load_state()
    assert "www.youtube.com/c/OrangeHRMInc" in youtube_new_page.url
    page.bring_to_front()
    expect(page).to_have_url ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    





