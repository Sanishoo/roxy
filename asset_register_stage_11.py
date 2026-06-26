# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: AssetRegister
import json, os

def save_to_file(data: dict, path: str = "assets.json") -> None:
    """Сохраняет состояние реестра в JSON файл с проверкой и форматированием."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {path}")
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить файл: {e}")

def load_from_file(path: str = "assets.json") -> dict | None:
    """Загружает данные из JSON файла или возвращает пустой словарь при ошибке."""
    if not os.path.exists(path):
        return {"assets": [], "owners": {}, "history": []}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстановление структуры данных при загрузке (если нужно преобразовать старые форматы)
        if not isinstance(data.get('assets'), list):
            data['assets'] = []
        return data
    except Exception:
        print("[WARN] Ошибка чтения файла, используется пустая структура.")
        return {"assets": [], "owners": {}, "history": []}

# Пример инициализации при старте приложения (вставьте этот вызов в начало main или модуля)
if __name__ == "__main__":
    initial_data = load_from_file()
    # Если файл не существует, создаётся автоматически с пустыми списками
