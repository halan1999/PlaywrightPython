from core.common_locators import CommonLocators as CL

class AnnouncementsLocators:
    ADD_NEW_BUTTON = CL._normalize_space_xpath("a", "Add New")
    HIDE_BUTTON = CL._normalize_space_xpath("a", "Hide")
    TITLE_INPUT = CL._input_by_attribute_xpath("name", "title")
    DEPARTMENT_SELECTBOX = "//span[@class='selection']"
    SUMMARY_INPUT = CL._input_by_attribute_xpath("id", "summary")
    START_DATE = CL._input_by_attribute_xpath("name", "start_date")
    END_DATE = CL._input_by_attribute_xpath("name", "end_date")
    RESET_BUTTON = CL._button_by_attribute_xpath("type", "reset")
    SAVE_BUTTON = CL._button_by_attribute_xpath("type", "submit")