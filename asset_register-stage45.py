# === Stage 45: Добавь восстановление из резервной копии ===
# Project: AssetRegister
def restore_from_backup(self, path):
        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError(f"Недопустимый формат резервной копии: {path}")
        
        if not isinstance(data, dict) or 'assets' not in data:
            raise ValueError("Неверная структура резервной копии")
        
        self._assets = data['assets']
        self._owners = data.get('owners', {})
        self._states = data.get('states', {})
        self._check_schedules = data.get('check_schedules', {})
        self._history = data.get('history', [])
        self._metadata = data.get('metadata', {})
        return len(self._assets)
