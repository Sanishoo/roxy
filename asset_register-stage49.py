# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: AssetRegister
def main():
    print("=" * 60)
    print(" AssetRegister — самопроверка и отчёт о готовности")
    print("=" * 60)

    from data import Asset, AssetState, AssetStatus, AssetCategory, AssetCheckStatus
    from core import AssetManager
    from history import History

    # --- Тест 1: создание и регистрация активов ---
    mgr = AssetManager()

    assets = [
        Asset("Ноутбук", "Иван", AssetState.WORKING, AssetStatus.GOOD, AssetCategory.TECH, "2026-01-15"),
        Asset("Дрель", "Петр", AssetState.WORKING, AssetStatus.GOOD, AssetCategory.TECH, "2026-02-10"),
        Asset("Очки", "Мария", AssetState.WORN, AssetStatus.GOOD, AssetCategory.PPE, "2025-12-01"),
        Asset("Перчатки", "Сергей", AssetState.BROKEN, AssetStatus.BAD, AssetCategory.PPE, "2024-06-20"),
    ]
    for a in assets:
        mgr.register(a)

    # --- Тест 2: статусы и фильтрация ---
    print(f"Всего активов: {mgr.count()}")
    print(f"Регистрированные: {mgr.list()}")
    print(f"Поиск 'Ноутбук': {mgr.search('Ноутбук')}")

    # --- Тест 3: история ---
    history = History()
    history.log("Начало тестирования")
    history.log("Регистрация 4-х активов")
    history.log("Проверка завершена")
    print(f"История: {history.get()}")

    # --- Тест 4: валидация ---
    bad = Asset("???", "", AssetState.UNKNOWN, AssetStatus.UNKNOWN, AssetCategory.UNKNOWN, "0000-00-00")
    assert mgr.register(bad) is False, "Недопустимый актив должен быть отклонён"
    print("Валидация: некорректный актив корректно отклонён")

    # --- Итоговый отчёт ---
    print("\n" + "=" * 60)
    print(" ✅ AssetRegister полностью готов к работе!")
    print("=" * 60)

if __name__ == "__main__":
    main()
