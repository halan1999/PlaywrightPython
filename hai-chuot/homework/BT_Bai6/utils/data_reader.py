import json, os
from pathlib import Path

class DataReader:
    ROOT = Path(__file__).resolve().parent.parent
    DATA_DIR = ROOT / "data"

    @staticmethod
    def read_json_data(file_name : str):
        path_file = DataReader.DATA_DIR / file_name

        with path_file.open("r", encoding="utf-8") as file:
            return json.load(file)