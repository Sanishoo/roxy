# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: AssetRegister
class _Favorites:
    def __init__(self):
        self._data = {}

    def add(self, key):
        if key not in self._data:
            self._data[key] = []
        self._data[key].append(key)

    def remove(self, key):
        if key in self._data:
            self._data[key] = [x for x in self._data[key] if x != key]

    def get(self):
        return list(self._data.values())

    def clear(self):
        self._data.clear()
