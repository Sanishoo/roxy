# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: AssetRegister
import json, sys, os
from pathlib import Path

def load_initial_data(json_string: str) -> dict[str, list[dict]]:
    """Импортирует начальные данные из JSON-строки и возвращает структуру реестра."""
    try:
        raw = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Неверный формат JSON: {e}")
        sys.exit(1)

    if not isinstance(raw, dict):
        print("[ERROR] Ожидается объект JSON с ключами 'assets' и 'owners'.")
        sys.exit(1)

    assets = raw.get("assets", [])
    owners = raw.get("owners", {})
    
    # Валидация структуры активов
    if not isinstance(assets, list):
        print("[ERROR] Ключ 'assets' должен содержать список.")
        sys.exit(1)

    for asset in assets:
        required_keys = {"id", "name", "owner_id", "status", "check_date"}
        missing = required_keys - set(asset.keys())
        if missing:
            print(f"[WARN] Актив {asset.get('id', 'unknown')} не имеет полей: {missing}")

    # Валидация владельцев (опционально, если они нужны для связей)
    for owner_id in [a["owner_id"] for a in assets]:
        if owner_id not in owners and "owners" in raw:
            print(f"[WARN] Владелец с ID {owner_id} не найден в списке 'owners'.")

    return {"assets": assets, "owners": owners}
