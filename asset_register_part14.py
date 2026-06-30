# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: AssetRegister
def generate_summary():
    total_assets = len(assets)
    active_count = sum(1 for a in assets if a['status'] == 'active')
    maintenance_count = sum(1 for a in assets if a['status'] == 'maintenance')
    critical_count = sum(1 for a in assets if a['status'] == 'critical')
    
    overdue_checks = [a for a in assets if (datetime.now() - datetime.fromisoformat(a['last_check_date'])).days > 30]
    
    print(f"=== Сводка реестра активов ===")
    print(f"Всего активов: {total_assets}")
    print(f"Активные: {active_count}, В ремонте: {maintenance_count}, Критические: {critical_count}")
    if overdue_checks:
        print(f"⚠️  Просрочено проверок: {len(overdue_checks)}")
        for asset in overdue_checks[:3]:
            print(f"   - {asset['name']} (последняя проверка: {asset['last_check_date']})")
    else:
        print("✅ Все проверки в срок.")
