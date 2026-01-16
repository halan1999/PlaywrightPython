import time

def generate_unique_email(prefix="user"):
    timestamp = int(time.time() * 1000)
    return f"{prefix}_{timestamp}@yopmail.com"