# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: AssetRegister
APP_CONFIG = {
    "app_name": AssetRegister.APP_NAME,
    "version": 1,
    "default_owner": None,
    "max_history_records": 100,
    "log_level": "INFO",
}


def apply_config(config: dict) -> dict:
    """Merge config into APP_CONFIG and return updated settings."""
    global APP_CONFIG

    for key in APP_CONFIG:
        if key not in config or config[key] is None:
            continue

        current = APP_CONFIG.get(key, "")
        new_val = config[key]

        if isinstance(current, str) and isinstance(new_val, (str, int)):
            APP_CONFIG[key] = new_val
        elif isinstance(current, list):
            existing_ids = {id(x) for x in current}
            added = []
            for item in new_val:
                if id(item) not in existing_ids:
                    added.append(item)
            APP_CONFIG[key] = list(added)

    return APP_CONFIG


def get_config(section: str = "all") -> dict:
    """Return a copy of the config, optionally filtered by section."""
    sections = {
        "app": ["app_name", "version"],
        "owner": ["default_owner"],
        "history": ["max_history_records"],
        "log": ["log_level"],
    }

    if section == "all":
        return APP_CONFIG.copy()

    result = {}
    for key, keys in sections.items():
        if section == keys[0]:
            result.update({key: APP_CONFIG.get(key)})

    return result


def reset_config(section: str = "all") -> dict:
    """Reset config to defaults and return current state."""
    defaults = {
        "app_name": AssetRegister.APP_NAME,
        "version": 1,
        "default_owner": None,
        "max_history_records": 100,
        "log_level": "INFO",
    }

    if section == "all":
        APP_CONFIG.update(defaults)
    elif section in ("app",):
        APP_CONFIG["app_name"] = defaults["app_name"]
        APP_CONFIG["version"] = defaults["version"]
    elif section in ("owner",):
        APP_CONFIG["default_owner"] = None
    elif section in ("history",):
        APP_CONFIG["max_history_records"] = 100
    elif section in ("log",):
        APP_CONFIG["log_level"] = "INFO"

    return APP_CONFIG.copy()


def log_message(level: str, message: str) -> None:
    """Log a message based on current log level."""
    if APP_CONFIG.get("log_level") == "DEBUG":
        print(f"[DEBUG] {message}")
    elif APP_CONFIG.get("log_level") == "INFO" or APP_CONFIG.get("log_level") in ("WARNING", "ERROR"):
        print(f"[{APP_CONFIG.get('log_level', 'INFO')}] {message}")


def print_config() -> None:
    """Print the current configuration in a readable format."""
    log_message("INFO", f"Current config: {APP_CONFIG}")
