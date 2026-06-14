# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: AssetRegister
def edit_asset(asset_id: str, updates: dict) -> bool | None:
    """Редактирует запись по ID, возвращая обновлённый объект или False."""
    if asset_id not in assets_registry:
        return False
    
    original = assets_registry[asset_id].copy()
    
    for key, value in updates.items():
        if key in ["id", "created_at"]:
            continue  # Запрещаем изменение идентификатора и времени создания
        
        if hasattr(original[key], 'append') and isinstance(value, list):
            original[key].extend(value)
        elif callable(getattr(original[key], 'update')):
            original[key].update(value)
        else:
            original[key] = value
    
    assets_registry[asset_id] = original
    audit_log.append({
        "action": "edit",
        "timestamp": datetime.now(),
        "asset_id": asset_id,
        "changes": {k: [original.get(k), value] for k in updates if k != "id"}
    })
    
    return assets_registry[asset_id]
