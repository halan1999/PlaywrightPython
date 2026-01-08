from faker import Faker
import uuid
# Khởi tạo faker với ngôn ngữ tiếng Việt nếu muốn data nhìn gần gũi
fake = Faker('vi_VN') 

def random_email(prefix="kimqa_"):
    return f"{prefix}{fake.email()}"

def random_phone():
    # Tạo số điện thoại Việt Nam ngẫu nhiên
    return fake.phone_number()

def random_address():
    return fake.address().replace("\n", ", ")

def random_uuid(length=5):
    # Tạo một UUID ngẫu nhiên, chuyển thành string và lấy 5 ký tự đầu tiên
    return str(uuid.uuid4())[:length]

def random_name(base_name="KimQA"):
    # Kết hợp tên gốc và chuỗi uuid 5 ký tự
    return f"{base_name}_{random_uuid()}"