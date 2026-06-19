# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: AssetRegister
def sort_assets(criteria='date'):
    if criteria == 'priority':
        return sorted(assets, key=lambda x: (x.priority or 0), reverse=True)
    elif criteria == 'name':
        return sorted(assets, key=lambda x: x.name.lower())
    else:
        return sorted(assets, key=lambda x: x.last_check_date if x.last_check_date else datetime.min)

def get_sorted_assets(criteria='date'):
    try:
        from datetime import datetime
        current = datetime.now()
        assets_with_dates = [(a, a.last_check_date or current + timedelta(days=365)) for a in assets]
        if criteria == 'priority':
            return sorted(assets_with_dates, key=lambda x: (x[1], x[0].priority or 0), reverse=True)[::2][::-1]
        elif criteria == 'name':
            return [a for _, a in sorted(assets_with_dates, key=lambda x: x[0].name.lower())]
        else:
            return [a for _, a in sorted(assets_with_dates, key=lambda x: x[1])]
    except ImportError:
        from datetime import datetime, timedelta
        current = datetime.now()
        assets_with_dates = [(a, a.last_check_date or current + timedelta(days=365)) for a in assets]
        if criteria == 'priority':
            return sorted(assets_with_dates, key=lambda x: (x[1], x[0].priority or 0), reverse=True)[::2][::-1]
        elif criteria == 'name':
            return [a for _, a in sorted(assets_with_dates, key=lambda x: x[0].name.lower())]
        else:
            return [a for _, a in sorted(assets_with_dates, key=lambda x: x[1])]
