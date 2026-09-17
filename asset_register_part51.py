# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: AssetRegister
class ChangeLog:
    def __init__(self):
        self._entries = []

    def log(self, asset_id, action, old_state, new_state):
        self._entries.append({
            'timestamp': datetime.now().isoformat(),
            'asset_id': asset_id,
            'action': action,
            'old_state': old_state,
            'new_state': new_state,
        })

    def get_history(self, asset_id=None):
        if asset_id is None:
            return self._entries
        return [e for e in self._entries if e['asset_id'] == asset_id]

    def clear(self):
        self._entries.clear()
