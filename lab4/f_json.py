import json


def save_json(data, path="result.json"):
    """json (вбудована): зберігає словник у файл."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return path
