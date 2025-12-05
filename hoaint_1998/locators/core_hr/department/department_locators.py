from core.common_locators import CommonLocators

class DepartmentLocator:
    SAVE_BUTTON = CommonLocators._normalize_space_xpath("span", "Save")
    NAME_INPUT = CommonLocators._input_by_attribute_xpath("name", "department_name")
