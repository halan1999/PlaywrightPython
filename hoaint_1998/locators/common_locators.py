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
