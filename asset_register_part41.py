# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: AssetRegister
def dry_run(action, asset_id, details=None):
    """Simulate a write operation without persisting and return a preview dict."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "status": "dry_run",
        "action": action,
        "asset_id": asset_id,
        "timestamp": now,
        "details": details or {},
    }
    if action in ("update", "replace"):
        entry["note"] = "Data was NOT written. Review the preview above, then re-run with a real write."
    return entry
