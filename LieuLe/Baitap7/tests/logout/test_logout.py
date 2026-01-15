def test_logout_from_header(dashboard):
    dashboard.do_logout(via="header")

def test_logout_from_body(dashboard):
    dashboard.do_logout(via="body")
