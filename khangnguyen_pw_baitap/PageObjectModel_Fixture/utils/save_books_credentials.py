import json
from pathlib import Path


def save_books_login_credential(
    email: str,
    password: str,
    file_path: str = "resources/books/login_credentials.json"
):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = json.loads(path.read_text(encoding="utf-8"))

    data.append({
        "email_address": email,
        "password": password
    })

    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
