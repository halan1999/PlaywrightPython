# utils/randoms.py
import random
import string

from data.books.street_address import STREET_ADDRESS

def random_suffix(length: int = 5) -> str:
    chars = string.ascii_lowercase + "123456789"
    return "".join(random.choice(chars) for _ in range(length))

def random_phone() -> str:
    return f"+84{random.randint(300000000, 999999999)}"

def random_address() -> str:
    house_number = random.randint(100, 300)
    street_address = random.choice(STREET_ADDRESS)
    return f"{house_number} {street_address}, Ho Chi Minh City"

def random_email() -> str:
    return f"test_khang0912_{random_suffix(5)}@email.com"