# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: AssetRegister
def filter_assets(status=None, category=None, tags=None):
    filtered = []
    for asset in assets:
        if status and asset.get('status') != status:
            continue
        if category and asset.get('category') != category:
            continue
        if tags:
            asset_tags = set(asset.get('tags', []))
            if not any(tag in asset_tags for tag in tags):
                continue
        filtered.append(asset)
    return filtered

def print_filtered_assets(filters=None, limit=10):
    status, category, tags = filters or (None, None, None)
    result = filter_assets(status=status, category=category, tags=tags)
    if not result:
        print("Нет записей по указанным критериям.")
        return
    for i, asset in enumerate(result[:limit], 1):
        print(f"{i}. {asset['id']}: {asset['name']} [{asset.get('category', 'N/A')}] - Статус: {asset.get('status', 'N/A')}")
        if tags and asset.get('tags'):
            print(f"   Теги: {', '.join(asset['tags'])}")
