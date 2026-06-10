# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: AssetRegister
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

class Asset:
    def __init__(self, id: str, name: str, owner: str, status: str, check_date: datetime):
        self.id = id
        self.name = name
        self.owner = owner
        self.status = status
        self.check_date = check_date

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "owner": self.owner,
            "status": self.status,
            "check_date": self.check_date.isoformat()
        }

class AssetRegister:
    def __init__(self):
        self.assets: List[Asset] = []
        self.history: List[Dict[str, Any]] = []

    def add_asset(self, asset: Asset) -> None:
        self.assets.append(asset)
        self._log_event(f"Добавлен актив {asset.name} (ID: {asset.id})", "create")

    def get_assets_by_owner(self, owner_name: str) -> List[Asset]:
        return [a for a in self.assets if a.owner == owner_name]

    def _log_event(self, message: str, event_type: str) -> None:
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "event": message,
            "type": event_type
        })

def main():
    register = AssetRegister()

    demo_assets = [
        Asset("A001", "Дрель Makita", "Иванов И.И.", "в норме", datetime.now() + timedelta(days=30)),
        Asset("A002", "Перфоратор Bosch", "Петров П.П.", "требует ремонта", datetime.now() + timedelta(days=5)),
        Asset("A003", "Шуруповерт DeWalt", "Сидоров С.С.", "в норме", datetime.now() + timedelta(days=60))
    ]

    for asset in demo_assets:
        register.add_asset(asset)

    print(f"Инициализация завершена. Всего активов: {len(register.assets)}")
    print("История событий:")
    for entry in register.history:
        print(f"  [{entry['timestamp']}] {entry['event']} ({entry['type']})")

if __name__ == "__main__":
    main()
