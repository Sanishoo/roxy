# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: AssetRegister
def generate_monthly_statistics(records, year=2024):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'checked': 0, 'overdue': 0})
    for r in records:
        if not isinstance(r['date'], str) or len(r['date']) != 10: continue
        month_key = f"{year}-{r['date'][5:7]}"
        stats[month_key]['total'] += 1
        if r.get('status') == 'checked': stats[month_key]['checked'] += 1
        check_date_str = r.get('check_date', '')
        if len(check_date_str) >= 6 and int(check_date_str[:4]) == year:
            current_month = int(r['date'][5:7])
            check_month = int(check_date_str[5:7])
            if check_month < current_month or (check_month == current_month and int(check_date_str[8:]) < int(r['date'][8:])):
                stats[month_key]['overdue'] += 1
    return dict(sorted(stats.items()))
