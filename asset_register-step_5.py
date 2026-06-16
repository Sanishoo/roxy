# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: AssetRegister
def delete_asset(asset_id: str) -> bool:
    if asset_id not in assets_registry:
        print(f"Ошибка: актив с ID {asset_id} не найден.")
        return False
    
    deleted_count = 0
    for key, value in list(assets_registry.items()):
        if value['id'] == asset_id:
            del assets_registry[key]
            deleted_count += 1
            
    print(f"Удалено записей о активе {asset_id}: {deleted_count}")
    return True

def get_asset_history(asset_id: str) -> list[dict]:
    history = []
    for key, value in assets_registry.items():
        if value['id'] == asset_id and 'history' in value:
            history.extend(value['history'])
    return sorted(history, key=lambda x: x.get('timestamp', ''), reverse=True)

def get_asset_status(asset_id: str) -> dict | None:
    for key, value in assets_registry.items():
        if value['id'] == asset_id:
            return {**value, 'status': value.get('condition', 'unknown')}
    return None
