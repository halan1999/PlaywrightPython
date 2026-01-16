import json
import os

def load_json_data(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'data', file_name)
    with open(data_path, encoding='utf-8') as f:
        return json.load(f)