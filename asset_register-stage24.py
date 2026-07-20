# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: AssetRegister
def show_record(asset_id, assets_db):
    if asset_id not in assets_db:
        print(f"Запись {asset_id} не найдена в реестре.")
        return
    a = assets_db[asset_id]
    print("=" * 60)
    print(f"ID:          {a['id']}")
    print(f"Наименование: {a.get('name', '—')}")
    print(f"Тип:         {a.get('type', '—')}")
    print(f"Владелец:    {a.get('owner_name', a.get('owner_id', '—'))}")
    if isinstance(a['status'], list):
        print(f"Статусы:     {', '.join(s.get('label', s) for s in a['status'])}")
    else:
        print(f"Статус:      {a['status']}")
    check = a.get('next_inspection')
    if isinstance(check, dict):
        print(f"След. проверка: {check.get('date', '—')} ({check.get('result', '')})")
    elif isinstance(check, str):
        print(f"След. проверка: {check}")
    else:
        print(f"След. проверка: —")
    print("=" * 60)
