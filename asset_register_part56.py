# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: AssetRegister
def bulk_update_assets(selected, field, value):
    for asset in selected:
        asset[field] = value
        asset['history'].append({
            'action': 'bulk_update',
            'field': field,
            'value': value,
            'timestamp': datetime.now().isoformat()
        })
    return len(selected)
