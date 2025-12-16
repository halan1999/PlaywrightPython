def test_capture_all(dashboard):
    dashboard.page.wait_for_url("**/erp/desk")
    dashboard.left_menu.capture_all()


