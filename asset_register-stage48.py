# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: AssetRegister
class _AssetRecord:
    def __init__(self, asset_id, owner, status, due_date, history):
        self.asset_id = asset_id
        self.owner = owner
        self.status = status
        self.due_date = due_date
        self.history = history

    def add_event(self, event_type, details):
        self.history.append({"type": event_type, "details": details, "timestamp": _utc_now()})

    def __repr__(self):
        return f"Asset({self.asset_id}, owner={self.owner}, status={self.status}, due={self.due_date})"


def _utc_now():
    import datetime
    return datetime.datetime.utcnow().isoformat()


class _AssetRegister:
    def __init__(self):
        self._assets = {}
        self._next_id = 1
        self._events = []

    def _new_id(self):
        self._next_id += 1
        return self._next_id

    def add_asset(self, asset_id, owner, status, due_date):
        if asset_id in self._assets:
            return None
        record = _AssetRecord(asset_id, owner, status, due_date, [])
        record.add_event("CREATED", {"owner": owner, "due_date": due_date})
        self._assets[asset_id] = record
        return record

    def get_asset(self, asset_id):
        return self._assets.get(asset_id)

    def update_status(self, asset_id, new_status):
        rec = self._assets.get(asset_id)
        if rec is None:
            return None
        old_status = rec.status
        rec.status = new_status
        rec.add_event("STATUS_CHANGED", {"from": old_status, "to": new_status})
        return rec

    def update_owner(self, asset_id, new_owner):
        rec = self._assets.get(asset_id)
        if rec is None:
            return None
        old_owner = rec.owner
        rec.owner = new_owner
        rec.add_event("OWNER_CHANGED", {"from": old_owner, "to": new_owner})
        return rec

    def set_due_date(self, asset_id, new_due_date):
        rec = self._assets.get(asset_id)
        if rec is None:
            return None
        old_due = rec.due_date
        rec.due_date = new_due_date
        rec.add_event("DUE_DATE_CHANGED", {"from": old_due, "to": new_due_date})
        return rec

    def get_history(self, asset_id):
        rec = self._assets.get(asset_id)
        if rec is None:
            return []
        return rec.history

    def get_all_assets(self):
        return list(self._assets.values())

    def get_due_soon(self, days=7):
        import datetime
        cutoff = datetime.datetime.utcnow() + datetime.timedelta(days=days)
        return [r for r in self._assets.values() if r.due_date <= cutoff]
