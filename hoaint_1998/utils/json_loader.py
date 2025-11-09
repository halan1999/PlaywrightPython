import json
import os

def load_json_file(file_path: str):
    try: 
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"[FILE] not found {file_path}")
    except json.JSONDecodeError as e:
        print(f"[JSON] json format error: {e}")
        return None
