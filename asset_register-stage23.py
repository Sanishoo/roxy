# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: AssetRegister
def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = len(str(val)) if val is not None else 0
            col_widths[i] = max(col_widths[i], w)

    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*headers))
    print("-+-".join("-" * w for w in col_widths))
    for row in rows:
        vals = [str(v) if v is not None else "" for v in row]
        print(fmt.format(*vals))

def display_assets(assets, history=None):
    headers = ["ID", "Name", "Owner", "Status", "Check Date", "Last Check"]
    rows = []
    for a in assets:
        check_date = str(a["check_date"]) if a["check_date"] else ""
        last_check = str(history[-1]["date"]) if history and history[-1].get("asset_id") == a["id"] else ""
        rows.append([a["id"], a["name"], a["owner"], a["status"], check_date, last_check])

    print_table(headers, rows)
