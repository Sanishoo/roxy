# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: AssetRegister
def backup_data_file(data_file_path, backup_dir=".backups"):
    import shutil, os
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    if not os.path.isfile(data_file_path):
        return None
    backup_name = f"{data_file_path}.bak"
    backup_path = os.path.join(backup_dir, backup_name)
    shutil.copy2(data_file_path, backup_path)
    return backup_path
