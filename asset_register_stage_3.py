# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: AssetRegister
class AssetRegister:
    def __init__(self):
        self._assets = {}
        self._history = []

    def add_asset(self, asset_id: str, owner: str, status: str, check_date: str) -> None:
        if asset_id in self._assets:
            raise ValueError(f"Актив {asset_id} уже существует")
        record = {"id": asset_id, "owner": owner, "status": status, "check_date": check_date}
        self._assets[asset_id] = record
        self._history.append({"action": "add", "data": record.copy()})

    def update_status(self, asset_id: str, new_status: str) -> None:
        if asset_id not in self._assets:
            raise KeyError(f"Актив {asset_id} не найден")
        old_record = self._assets[asset_id].copy()
        old_record["status"] = new_status
        self._history.append({"action": "update", "data": old_record, "new_status": new_status})

    def get_asset(self, asset_id: str) -> dict | None:
        return self._assets.get(asset_id)

    def list_assets(self) -> list[dict]:
        return list(self._assets.values())
