from utils.randoms import *

class MePayload:
    def __init__(self, access_token):
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def to_dict(self):
        return self.__dict__

class MeResponse:
    def __init__(self, json_data):

        self.id = json_data.get("id")
        self.name = json_data.get("name")
        self.email = json_data.get("email")
        self.avatarurl = json_data.get("avatarUrl")
        self.phone = json_data.get("phone")
        self.address = json_data.get("address")
        self.config = json_data.get("config")
        
    def assert_matches_payload(self, payload: dict):
        """
        Hàm so sánh linh động object hiện tại với một payload bất kỳ.
        Loại bỏ ID vì ID thường do Server sinh ra, không có trong payload gửi đi.
        """
        for key, expected_value in payload.items():
            # Đồng bộ key của payload với thuộc tính của class
            attr_name = "avatarurl" if key == "avatarUrl" else key
            
            actual_value = getattr(self, attr_name, None)
            assert actual_value == expected_value, (
                f"Mismatched field: {key}. "
                f"Expected: {expected_value}, Actual: {actual_value}"
            )