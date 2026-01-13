import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_avatar_path():
    return os.path.join(BASE_DIR, "tests", "data", "avatar.png")
