# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: AssetRegister
def validate_date(date_str, field_name):
    """Проверяет корректность даты в формате ГГГГ-ММ-ДД."""
    try:
        parts = date_str.split('-')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise ValueError("Неверный формат даты")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if month < 1 or month > 12:
            raise ValueError("Месяц вне диапазона 1-12")
        if day < 1 or day > 31:
            raise ValueError("День вне диапазона 1-31")
        return True, date_str
    except Exception as e:
        return False, str(e)

def format_date(date_str):
    """Форматирует дату в стандартный вид."""
    if validate_date(date_str, "Дата")[0]:
        parts = date_str.split('-')
        return f"{parts[2]}.{parts[1]}.{parts[0]}"
    else:
        return "Неизвестная дата"

def get_days_until_expiry(expiry_date):
    """Вычисляет количество дней до истечения срока проверки."""
    from datetime import date, timedelta
    valid, _ = validate_date(expiry_date, "Дата истечения")
    if not valid:
        return None
    try:
        target = date.fromisoformat(expiry_date)
        today = date.today()
        days_left = (target - today).days
        if days_left < 0:
            return f"Срок истёк {abs(days_left)} дней назад"
        elif days_left == 0:
            return "Срок истекает сегодня"
        else:
            return str(days_left) + " день(ов)"
    except Exception as e:
        return f"Ошибка расчёта срока: {e}"
