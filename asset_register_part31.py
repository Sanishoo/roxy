# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: AssetRegister
class UserProfile:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role

    @staticmethod
    def get_current_profile():
        return _current_profile if _current_profile else UserProfile("default_user")

    @staticmethod
    def set_current_profile(profile):
        global _current_profile
        _current_profile = profile

_current_profile = None


def switch_active_profile(name, role="user"):
    new_profile = UserProfile(name, role)
    _current_profile = new_profile
    print(f"Active profile switched to: {new_profile.name} ({new_profile.role})")
