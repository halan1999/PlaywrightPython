from faker import Faker
import random
import string

def _get_random_test(lenght:int=10):
    """
    Trả về dải ký dự gồm letters và digits
    mặc định chiều dài là 10
    """
    otp = ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))
    value = f"hoai_{otp}"
    return value