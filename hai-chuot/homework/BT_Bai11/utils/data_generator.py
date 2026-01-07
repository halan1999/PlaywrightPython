from datetime import datetime
import random

class DataGenerator:
    @staticmethod
    def generate_email():
        now = datetime.now()
        time_string = now.strftime("%d%m%Y%H%M%S")
        return f"tony.rat{time_string}@chuotbeo.tester.vn"

    @staticmethod
    def generate_name():
        last_name = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ"]
        middle_name = ["Văn", "Thị", "Minh", "Anh", "Đức", "Thanh", "Ngọc", "Bảo", "Gia", "Khánh"]
        first_name = ["An", "Bình", "Chi", "Dũng", "Em", "Giang", "Hương", "Khôi", "Linh", "Nam", "Oanh", "Phúc", "Quang", "Sơn", "Thảo", "Uyên", "Việt", "Xuân", "Yến", "Khoa"]
        last_name_choice = random.choice(last_name)
        middle_name_choice = random.choice(middle_name)
        first_name_choice = random.choice(first_name)
        return f"{last_name_choice} {middle_name_choice} {first_name_choice}"

    @staticmethod
    def generate_phone():
        list_prefix_phone = [
            "032", "033", "034", "035", "036", "037", "038", "039",
            "056", "058", "059",
            "070", "076", "077", "078", "079",
            "081", "082", "083", "084", "085", "086", "088", "089",
            "090", "091", "092", "093", "094", "096", "097", "098", "099"
        ]

        prefix_phone = random.choice(list_prefix_phone)
        suffix_phone = "".join([str(random.randint(0, 9)) for _ in range(7)])

        return f"{prefix_phone}{suffix_phone}"