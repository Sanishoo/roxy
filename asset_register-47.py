# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: AssetRegister
def demo():
    """Показывает основной пользовательский сценарий работы с реестром активов."""
    register = AssetRegister()
    register.add_asset("Laptop", owner="Ivan", status="active", check_date=20260315)
    register.add_asset("Projector", owner="Maria", status="maintenance", check_date=20260520)
    register.add_asset("Drill", owner="Oleg", status="retired", check_date=20250110)

    print(f"Всего активов: {len(register.assets)}")
    print(f"Активные: {sum(1 for a in register.assets if a['status'] == 'active')}")
    print(f"В ремонте: {sum(1 for a in register.assets if a['status'] == 'maintenance')}")
    print(f"Неактивные: {sum(1 for a in register.assets if a['status'] == 'retired')}")

    register.check_assets()
    print(f"Проверено: {register.checked_count}/{len(register.assets)}")

    register.add_asset("Cable", owner="Ivan", status="active", check_date=20260315)
    register.get_history("Ivan")
    print(f"Записи для Ивана: {len(register.get_history('Ivan'))}")
    register.close()
