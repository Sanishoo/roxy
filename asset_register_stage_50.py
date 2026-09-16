# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: AssetRegister
def print_report():
    """Выводит сводку по всем активам: статус, владелец, срок проверки."""
    print("=" * 60)
    print("Отчёт по реестру активов")
    print("=" * 60)
    for asset in assets:
        print(f"\n[{asset['id']}] {asset['name']}")
        print(f"  Статус:          {asset['status']}")
        print(f"  Владелец:        {asset['owner']}")
        print(f"  Срок проверки:   {asset['inspection_date']}")
        if asset['history']:
            print(f"  История:         {asset['history']}")
    print("\n" + "=" * 60)
