# payloads/register_payload.py
from utils.randoms import random_email, random_phone, random_address

registered_name = "Khang Nguyen"
registered_password = "Khang@qa1234"
registered_avatar_url = "https://i.pinimg.com/1200x/3e/f6/5f/3ef65f3dd78411b183c7e59106d2e1c5.jpg"

def build_register_payload() -> dict:
    return {
        "name": registered_name,
        "email": random_email(),
        "password": registered_password,
        "avatarUrl": registered_avatar_url,
        "phone": random_phone(),
        "address": random_address(),
    }