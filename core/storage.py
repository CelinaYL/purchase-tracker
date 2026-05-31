import json
import os

DATA_FILE = "data/purchases.json"

def load_purchases():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_purchases(purchases):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(purchases, file, ensure_ascii=False, indent=4)