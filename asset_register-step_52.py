# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: AssetRegister
def export_report(assets: list[Asset], history: list[History]) -> str:
    lines = ["=== Asset Register Report ===", f"Total assets: {len(assets)}"]
    for a in assets:
        lines.append(f"\n[{a.status}] {a.name} - Owner: {a.owner}, Check due: {a.check_date}")
    lines.append(f"\nTotal history entries: {len(history)}")
    return "\n".join(lines)
