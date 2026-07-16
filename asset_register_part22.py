# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: AssetRegister
class ReminderChecker:
    def __init__(self, register):
        self.register = register

    def check_overdue(self):
        overdue_assets = []
        for asset in self.register.assets.values():
            if asset.status == "active" and asset.next_inspection <= date.today() and (asset.last_reminder is None or asset.last_reminder < asset.next_inspection - timedelta(days=30)):
                overdue_assets.append(asset)
        return overdue_assets

    def notify_overdue(self, overdue_assets):
        for asset in overdue_assets:
            print(f"Напоминание: актив '{asset.name}' просрочен на проверку")
