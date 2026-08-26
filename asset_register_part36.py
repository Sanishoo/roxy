# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: AssetRegister
def verify_and_fix_assets():
    """Проверка целостности данных и авто-ремонт простых проблем."""
    issues = []
    for asset in assets:
        if not asset.get('status'):
            issues.append(('Asset', asset['id'], 'missing status', asset))
        if not asset.get('owner'):
            issues.append(('Asset', asset['id'], 'missing owner', asset))
        if not asset.get('inspection_date'):
            issues.append(('Asset', asset['id'], 'missing inspection_date', asset))
        if asset.get('status') in ('pending', 'maintenance') and not asset.get('history'):
            issues.append(('Asset', asset['id'], 'missing history for active status', asset))
    if issues:
        for issue in issues:
            asset = issue[3]
            if issue[1] == 'missing status':
                asset['status'] = 'unknown'
            elif issue[1] == 'missing owner':
                asset['owner'] = 'unassigned'
            elif issue[1] == 'missing inspection_date':
                asset['inspection_date'] = None
            elif issue[1] == 'missing history for active status':
                asset['history'] = []
        print(f"Fixed {len(issues)} integrity issues.")
    else:
        print("All assets are valid.")
    return issues
