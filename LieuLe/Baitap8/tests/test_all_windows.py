from playwright.sync_api import expect

def test_all_windows(login_page):
    login_page.open()
    login_page._open_all_social_tabs()

    print("Tabs saved:", login_page.list_tabs())
    # → ['linkedin', 'facebook', 'twitter', 'youtube']

    facebook = login_page.get_tab("facebook")
    assert facebook is not None
    facebook.bring_to_front()

    print("Facebook URL:", facebook.url)
    assert "facebook" in facebook.url.lower()

    linkedin = login_page.get_tab("linkedin")
    linkedin.bring_to_front()

    print("LinkedIn URL:", linkedin.url)
    assert "linkedin" in linkedin.url.lower()

    for name in login_page.list_tabs():
        tab = login_page.get_tab(name)
        print(f"[{name}] => {tab.url}")
