# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: AssetRegister
class Asset:
    def __init__(self, name: str, owner: str, status: str = "active", check_date: str | None = None):
        self.name = name.strip()
        self.owner = owner.strip()
        if not self._validate_owner(owner):
            raise ValueError(f"Недопустимый владелец: {owner}")
        if not self._validate_status(status):
            raise ValueError(f"Недопустимое состояние: {status}")
        self.status = status.lower()
        self.check_date = check_date

    def _validate_owner(self, owner: str) -> bool:
        return len(owner.strip()) > 0 and "@" in owner or "ИП" in owner or "ООО" in owner

    def _validate_status(self, status: str) -> bool:
        valid_statuses = {"active", "maintenance", "retired"}
        return status.lower() in valid_statuses
