import json
import os

def load_project_data():
    file_path = os.path.join(os.path.dirname(__file__), "project_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
