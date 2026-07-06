# === Stage 17: Добавь группировку записей по категориям ===
# Project: AssetRegister
CATEGORY_CHOICES = ["Оборудование", "Транспорт", "Электроника", "Инструменты", "Мебель", "Спецтехника"]


def add_category(asset_id, category_name):
    """Присвоить активу категорию."""
    if asset_id not in _assets:
        raise KeyError(f"Актив {asset_id} не найден")
    cat = category_name.strip()
    if cat not in CATEGORY_CHOICES:
        raise ValueError(
            f"Недопустимая категория. Выберите из: {', '.join(CATEGORY_CHOICES)}"
        )
    _assets[asset_id]["category"] = cat
    history_entry = {
        "id": _next_id,
        "type": "update",
        "field": "category",
        "value": cat,
        "timestamp": datetime.now(),
        "user": "admin",
    }
    history.append(history_entry)


def list_assets_by_category(category=None):
    """Получить активы по категории; если category=None — все."""
    result = _assets.copy() if category is None else {k: v for k, v in _assets.items() if v.get("category") == category}
    return sorted(result.values(), key=lambda a: (a["status"], a["id"]))


def get_category_stats():
    """Статистика по категориям."""
    stats = {}
    for asset_id, info in _assets.items():
        cat = info.get("category") or "Не назначена"
        stats[cat] = stats.get(cat, 0) + 1
    return stats
