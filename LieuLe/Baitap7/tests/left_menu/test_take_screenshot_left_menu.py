def test_capture_left_menu(left_menu_component):
    folder = "screenshots/left_menu"
    left_menu_component.capture_parent_menus(folder)
    left_menu_component.capture_submenus(folder)
