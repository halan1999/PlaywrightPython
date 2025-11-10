# utils/data_loader.py
import json
from pathlib import Path
from typing import List, Dict
import openpyxl

ROOT = Path(__file__).resolve().parent.parent

def load_users_from_json(path: str = None) -> List[Dict]:
    p = Path(path) if path else ROOT / "resources" / "users.json"
    with p.open(encoding="utf-8") as f:
        return json.load(f)

def load_users_from_excel(path: str = None) -> List[Dict]:
    p = Path(path) if path else ROOT / "resources" / "users.xlsx"
    wb = openpyxl.load_workbook(p)
    sheet = wb.active
    rows = list(sheet.iter_rows(values_only=True))
    if not rows:
        return []
    headers = [h.strip() for h in rows[0]]
    users = []
    for row in rows[1:]:
        if all(cell is None for cell in row):
            continue
        entry = {headers[i]: row[i] for i in range(len(headers))}
        # normalize keys
        users.append({
            "username": str(entry.get("username") or entry.get("user") or "").strip(),
            "password": str(entry.get("password") or "").strip(),
            "expected": str(entry.get("expected") or "success").strip().lower()
        })
    return users
