# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: AssetRegister
def search_assets(criteria, case_insensitive=True):
    results = []
    for asset in assets:
        match = True
        if 'name' in criteria and criteria['name']:
            if case_insensitive:
                if not criteria['name'].lower() in asset['name'].lower():
                    match = False
            else:
                if criteria['name'] != asset['name']:
                    match = False
        if 'owner' in criteria and criteria['owner']:
            if case_insensitive:
                if not criteria['owner'].lower() in asset['owner'].lower():
                    match = False
            else:
                if criteria['owner'] != asset['owner']:
                    match = False
        if 'status' in criteria and criteria['status']:
            if case_insensitive:
                if not criteria['status'].lower() in asset['status'].lower():
                    match = False
            else:
                if criteria['status'] != asset['status']:
                    match = False
        if 'check_date_min' in criteria and criteria['check_date_min']:
            if asset.get('check_date', '') < criteria['check_date_min']:
                match = False
        if 'check_date_max' in criteria and criteria['check_date_max']:
            if asset.get('check_date', '') > criteria['check_date_max']:
                match = False
        if match:
            results.append(asset)
    return results
