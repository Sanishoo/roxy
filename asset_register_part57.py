# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: AssetRegister
def bulk_delete(assets, ids, confirm=True):
    if confirm and not _prompt_yes(f"Удалить выбранные активы (id: {', '.join(map(str, ids))})?"):
        return 0
    removed = [a for a in assets if a['id'] in set(ids)]
    for a in removed:
        a['history'].append({'action': 'deleted', 'timestamp': datetime.now().isoformat()})
    assets[:] = [a for a in assets if a['id'] not in set(ids)]
    return len(removed)


def _prompt_yes(msg):
    try:
        return input(f"{msg} [y/N]: ").strip().lower() in ('y', 'yes')
    except (EOFError, KeyboardInterrupt):
        return False
