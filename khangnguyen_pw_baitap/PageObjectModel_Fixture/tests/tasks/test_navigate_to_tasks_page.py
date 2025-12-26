from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.tasks_page import TasksPage
from components.header_component import HeaderComponent

def test_tasks_menu_displayed(logged_in_page):
    home_page = HomePage(logged_in_page)
    assert home_page.is_tasks_menu_visible()

def test_navigate_to_tasks_page(logged_in_page):
    home_page = HomePage(logged_in_page)

    home_page.click_menu_item("Tasks")

    tasks_page = TasksPage(logged_in_page)
    tasks_page.is_tasks_page_loaded()

# def test_click_header_item_calendar(logged_in_page):
#     tasks_page = TasksPage(logged_in_page)
#     tasks_page.click_header_item("calendar") 

# def test_click_header_item_kanban(logged_in_page):
#     tasks_page = TasksPage(logged_in_page)
#     tasks_page.click_header_item("kanban") 