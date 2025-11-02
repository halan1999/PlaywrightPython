from pathlib import Path
import json

CREDENTIALS_FILE = Path(__file__).with_name("login_credentials.json")

def _load_all():
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_credentials(kind: str = "valid") -> tuple[str, str]:
    data = _load_all()[kind]
    return data["username"], data["password"]

def get_valid():   
    return get_credentials("valid")

def get_invalid():
    return get_credentials("invalid")
