# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: AssetRegister
def _soft_dedup(self, record):
    key_fields = ['name', 'identifier']
    existing = self._records
    for k in key_fields:
        if record.get(k) in existing:
            for r in existing:
                if r.get(k) == record.get(k):
                    return False
    return True
