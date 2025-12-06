from pages.Multi_Tabs.windows import Windows
from pages.Multi_Tabs.new_windows import NewWindows

def test_open_new_window(page):
    windows = Windows(page)
    windows._go_to_windows()
    new_window : NewWindows = windows.open_new_window()
    new_window._verify_page()
    # quay lại page ban đầu
    new_window._bring_to_font()