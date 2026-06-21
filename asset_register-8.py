# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: AssetRegister
def main_menu():
    while True:
        print("\n=== Меню AssetRegister ===")
        print("1. Просмотр списка активов")
        print("2. Добавить актив")
        print("3. Изменить владельца/состояние")
        print("4. Проверить сроки обслуживания")
        print("5. Показать историю изменений")
        print("6. Экспорт в CSV")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            for asset in assets:
                print(f"\nID: {asset['id']}, Название: {asset['name']}, Владелец: {asset.get('owner', 'N/A')}, Статус: {asset['status']}")
        elif choice == "2":
            name = input("Название актива: ")
            owner = input("Владелец: ")
            status = input("Статус (active/maintenance): ")
            assets.append({"id": len(assets) + 1, "name": name, "owner": owner, "status": status})
        elif choice == "3":
            idx = int(input("ID актива для изменения: ")) - 1
            if 0 <= idx < len(assets):
                new_owner = input(f"Новый владелец (нажмите Enter, чтобы оставить {assets[idx]['owner']}): ") or assets[idx]['owner']
                new_status = input(f"Новый статус (нажмите Enter, чтобы оставить {assets[idx]['status']}): ") or assets[idx]['status']
                if new_owner != assets[idx]['owner']:
                    log_history.append({"action": "change_owner", "asset_id": idx + 1, "old_value": assets[idx]['owner'], "new_value": new_owner})
                if new_status != assets[idx]['status']:
                    log_history.append({"action": "change_status", "asset_id": idx + 1, "old_value": assets[idx]['status'], "new_value": new_status})
                assets[idx]["owner"] = new_owner
                assets[idx]["status"] = new_status
        elif choice == "4":
            today = datetime.date.today()
            for asset in assets:
                if 'next_check' in asset and asset['next_check']:
                    days_left = (asset['next_check'] - today).days
                    print(f"{asset['name']} ({asset['owner']}): Проверка через {days_left} дней")
        elif choice == "5":
            for entry in reversed(log_history[-10:]):
                print(entry)
        elif choice == "6":
            import csv
            with open("assets.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "name", "owner", "status"])
                writer.writeheader()
                writer.writerows(assets)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
