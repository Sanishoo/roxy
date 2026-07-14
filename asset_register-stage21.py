# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: AssetRegister
import datetime

def get_due_date():
    return datetime.date.today()

def is_overdue(asset):
    if not asset.get("inspection_date"):
        return False
    due = datetime.datetime.strptime(asset["inspection_date"], "%Y-%m-%d").date()
    return datetime.date.today() > due

def format_due_info(asset):
    status = "✅ В срок" if not is_overdue(asset) else "⚠️ Просрочен"
    date_str = asset.get("inspection_date", "не указано")
    owner = asset.get("owner", {}).get("name", "нет владельца")
    return f"{status} | Владелец: {owner} | Срок проверки: {date_str}"

def print_due_notifications():
    overdue_assets = [a for a in assets if is_overdue(a)]
    if not overdue_assets:
        print("🎉 Все активы в норме! Напоминаний нет.")
        return
    print("\n⚠️ НАПОМИНАНИЯ — просроченные активы:")
    for asset in overdue_assets:
        info = format_due_info(asset)
        print(f"  • {info}")
