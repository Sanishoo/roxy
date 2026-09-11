# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: AssetRegister
def migrate_v46():
    """Migration v46: add version field to asset records for future schema evolution."""
    global _VERSION
    _VERSION = 46
    return _VERSION
