import json
import os

# Đường dẫn tới file lưu dữ liệu
DATA_FILE = "project_data.json"

def save_project_title(title: str):
    with open(DATA_FILE, "w") as f:
        json.dump({"projectTitle": title}, f)

def load_project_title() -> str:
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("Not found project_data.json, run test create project first!")
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data["projectTitle"]