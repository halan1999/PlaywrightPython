import csv
import os

def load_csv_data(file_path):
    data = []
    abs_path = os.path.abspath(file_path)
    with open(file=abs_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
