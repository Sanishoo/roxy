# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: AssetRegister
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "assets": [
            {
                "id": a["id"],
                "name": a["name"],
                "owner_id": a.get("owner_id"),
                "status": a["status"],
                "next_check": a["next_check"].strftime("%Y-%m-%d") if isinstance(a["next_check"], datetime) else str(a["next_check"]),
                "history_count": len(a.get("history", []))
            } for a in assets_registry.values()
        ],
        "owners": {oid: {"name": data["name"]} for oid, data in owners_registry.items()}
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
