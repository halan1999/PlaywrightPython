import json
import os

def read_json(relative_path):
    base_dir = os.path.dirname(os.path.dirname(__file__))  

    file_path = os.path.join(base_dir, relative_path)

    with open(file_path, encoding="utf-8") as f:
        print("Reading JSON from:", file_path)

        return json.load(f)
