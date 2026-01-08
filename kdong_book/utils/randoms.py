from faker import Faker
import uuid
fake = Faker('vi_VN') 

def random_email(prefix="kimqa_"):
    return f"{prefix}{fake.email()}"

def random_phone():
    return fake.phone_number()

def random_address():
    return fake.address().replace("\n", ", ")

def random_uuid(length=5):
    return str(uuid.uuid4())[:length]

def random_name(base_name="KimQA"):
    return f"{base_name}_{random_uuid()}"