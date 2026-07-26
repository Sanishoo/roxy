# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: AssetRegister
def print_metrics():
    n_assets = len(assets)
    if not assets:
        return print("Метрики недоступны — реестр пуст.")
    
    statuses = [a["status"] for a in assets]
    owners = set(a["owner"] for a in assets)
    expiring_30d = sum(1 for a in assets if a.get("expiry_date") and (datetime.now() + timedelta(days=30)).date() >= datetime.strptime(a["expiry_date"], "%Y-%m-%d").date())
    
    print(f"  Активов: {n_assets}")
    print(f"  Уникальных владельцев: {len(owners)}")
    print(f"  Состояний: {set(statuses)}")
    print(f"  Скоро истекают (30 дней): {expiring_30d}")

try:
    print_metrics()
except Exception as e:
    print(f"Ошибка при расчёте метрик: {e}")
