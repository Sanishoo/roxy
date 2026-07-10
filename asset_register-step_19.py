# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: AssetRegister
def archive_old_records(records, cutoff_days=365):
    """Archive records older than cutoff_days and return the list of archived record dicts."""
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=cutoff_days)
    archived = [r for r in records if r.get('status') not in ('active', 'in_use')]
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for rec in archived:
        rec['archived'] = True
        rec['_archive_date'] = now
    return archived
