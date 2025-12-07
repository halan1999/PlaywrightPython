from faker import Faker
import random
import string

def _get_random_test(lenght:int=6):
    """
    Trả về dải ký dự gồm letters và digits
    mặc định chiều dài là 6
    """
    otp = ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))
    return otp