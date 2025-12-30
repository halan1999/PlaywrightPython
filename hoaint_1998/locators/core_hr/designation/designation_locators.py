from core.common_locators import CommonLocators as CL

class DesignationLocators:
    DESIGNATION_TAB = CL._xpath_tab_by_href("designation")
    DEPARTMENT_SELECTBOX = "//span[@class='selection']"
    DEPARTMENT_INPUT = "//span[@class='select2-results']/preceding-sibling::span//input"
    DEPARTMENT_ITEM_IN_LIST = lambda name: f"//span[@class='select2-results']//li[normalize-space()='{name}']"
    DESIGNATION_NAME_INPUT = CL._input_by_attribute_xpath("name", "designation_name")
    DESCRIPTION_TEXTAREA = "//textarea[@name='description']"
    SAVE_BUTTON = CL._normalize_space_xpath("span", "Save")