# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: AssetRegister
def calculate_weekly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'failures': 0})
    for r in records:
        if isinstance(r['date'], str):
            try:
                date_obj = datetime.strptime(r['date'], '%Y-%m-%d')
            except ValueError:
                continue
        else:
            date_obj = r['date']
        week_start = (date_obj - timedelta(days=date_obj.weekday())).isoformat()
        stats[week_start]['count'] += 1
        if r.get('status') in ('failed', 'critical'):
            stats[week_start]['failures'] += 1
    return {k: {'total': v['count'], 'errors': v['failures']} for k, v in sorted(stats.items())}
