# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: AssetRegister
import random, string, datetime

def reset_demo_data():
    """Сбрасывает все данные в дефолтные значения."""
    for asset in assets:
        asset["owner"] = "Unknown"
        asset["status"] = "Active"
        asset["last_check"] = None
        asset["next_check"] = None
        asset["history"] = []

def clear_state():
    """Очищает историю проверок для всех активов."""
    for asset in assets:
        asset["history"].clear()

def fill_demo_data(count=5):
    statuses = ["Active", "Maintenance", "Retired", "Pending"]
    owners = [f"User_{i}" for i in range(1, 6)]
    prefixes = ["ASSET_", "COMPONENT_", "SENSOR_"]
    assets.clear()
    for _ in range(count):
        prefix = random.choice(prefixes)
        asset_id = f"{prefix}{random.randint(1000,9999)}"
        status = random.choice(statuses)
        owner = random.choice(owners)
        last_check_str = None
        next_check_str = None
        if status != "Retired":
            d = datetime.timedelta(days=random.randint(1, 365))
            now = datetime.datetime.now()
            last_check_str = (now - d).strftime("%Y-%m-%d %H:%M")
            next_check_str = (now + d).strftime("%Y-%m-%d %H:%M")
        history = []
        if status != "Active":
            for _ in range(random.randint(1,3)):
                check_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 90))
                result = random.choice(["OK", "Warning", "Error"])
                history.append({"date": check_date.strftime("%Y-%m-%d %H:%M"), "result": result})
        assets.append({
            "id": asset_id,
            "name": f"Demo Asset {len(assets)+1}",
            "owner": owner,
            "status": status,
            "last_check": last_check_str,
            "next_check": next_check_str,
            "history": history
        })
