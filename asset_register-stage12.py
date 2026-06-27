# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: AssetRegister
import json, os, sys
from pathlib import Path

def load_assets_from_file(file_path: str) -> list[dict]:
    try:
        with open(Path(file_path), 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data.get('assets', [])
            elif isinstance(data, list):
                return data
            else:
                print("Ошибка: некорректный формат JSON файла.")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        sys.exit(1)

if __name__ == '__main__':
    file_name = 'assets_backup.json'
    if os.path.exists(file_name):
        loaded_assets = load_assets_from_file(file_name)
        print(f"Загружено активов из '{file_name}': {len(loaded_assets)}")
        for asset in loaded_assets[:3]:
            print(asset['id'], '-', asset.get('status', 'unknown'))
