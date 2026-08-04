# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: AssetRegister
TEMPLATES = {}

def add_template(name, **fields):
    TEMPLATES[name] = fields.copy()

def create_from_template(template_name, overrides=None):
    if template_name not in TEMPLATES:
        raise ValueError(f"Template '{template_name}' does not exist")
    base = TEMPLATES[template_name].copy()
    if overrides:
        base.update(overrides)
    return base

add_template("sensor", owner="Lab", status="active", check_interval=7, last_check=None, history=[])
add_template("laptop", owner="DevOps", status="deployed", check_interval=30, last_check=None, history=[])
