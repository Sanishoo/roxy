# === Stage 32: Добавь журнал действий пользователя ===
# Project: AssetRegister
class ActionLog:
    """Журнал всех пользовательских действий в системе."""

    def __init__(self):
        self._entries = []

    def log(self, action_type: str, asset_id: int | None = None, user: str = "unknown", detail: str = "") -> dict:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "asset_id": asset_id,
            "user": user,
            "detail": detail,
        }
        self._entries.append(entry)
        return entry.copy()

    def get_log(self, limit: int = 50) -> list[dict]:
        return self._entries[-limit:]

    def clear(self):
        self._entries.clear()


action_log = ActionLog()
