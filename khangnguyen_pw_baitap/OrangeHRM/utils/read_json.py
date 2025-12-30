import json
import os


def read_json(file_path):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_dir, file_path)

    with open(full_path, "r") as f:
        return json.load(f)