class CommonLocators:
    @staticmethod
    def _input_by_attribute_xpath (attribute: str, value: str) -> str:
        return f"//input[@{attribute}='{value}']"
    
    @staticmethod
    def _button_by_attribute_xpath (attribute: str, value: str) -> str:
        return f"//button[@{attribute}='{value}']"
    
    @staticmethod
    def _contains_text_xpath (tag: str, value: str) -> str:
        return f"//{tag}[contains(text(), '{value}')]"
    
    @staticmethod
    def _normalize_space_xpath (tag: str, value: str) -> str:
        return f"//{tag}[normalize-space()='{value}']"
    
    @staticmethod
    def _attribute_data_original_title_xpath(tag: str, value: str) -> str:
        return f"//{tag}[@data-original-title='{value}']"
