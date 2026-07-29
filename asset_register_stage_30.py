# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: AssetRegister
def add_user_profile(name, role="operator"):
    profiles = {p["name"]: p for p in user_profiles}
    if name in profiles and profiles[name]["password"] != get_password_hash("oldpass"):
        raise ValueError(f"Profile '{name}' already exists with different password")
    user_profiles.append({"name": name, "role": role})
