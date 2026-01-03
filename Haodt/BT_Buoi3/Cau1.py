from playwright.sync_api import Page

def test_bach_due(page: Page):
    # Truy cập trang
    page.goto("https://the-internet.herokuapp.com/tables")

    # Tìm ô chứa chữ Batch
    xpath_due = "//table[@id='table1']//td[text()='Bach']/following-sibling::td[3]"

    # Lấy nội dung ô "Due"
    due_amount = page.locator(xpath_due).inner_text()

    print(f"Số tiền nợ (Due) của Bach là: {due_amount}")

    # Kiểm tra giá trị đúng
    assert due_amount == "$51.00"
