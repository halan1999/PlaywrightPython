from core.common_locators import CommonLocators

class DepartmentLocator:
    DEPARTMENT_TAB = CommonLocators._xpath_tab_by_href("department")
    # FORM ADD
    SAVE_BUTTON = CommonLocators._normalize_space_xpath("span", "Save")
    NAME_INPUT = CommonLocators._input_by_attribute_xpath("name", "department_name")
    # POPUP UPDATE
    NAME_INPUT_EDIT_POPUP = "//div[@id='ajax_view_modal']//input[@name='department_name']"
