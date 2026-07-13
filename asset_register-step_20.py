# === Stage 20: Добавь восстановление записей из архива ===
# Project: AssetRegister
def restore_from_archive(self, archive_path: str) -> int:
        """Восстанавливает записи из архива CSV/JSON файла. Возвращает число восстановленных записей."""
        import csv, json
        count = 0
        with open(archive_path, 'r') as f:
            content = f.read()
        if content.strip().endswith('.json'):
            records = json.loads(content)
        else:
            import io
            reader = csv.DictReader(io.StringIO(content))
            records = list(reader)
        for rec in records:
            self.add_record({**rec, 'archived': False})
            count += 1
        return count
