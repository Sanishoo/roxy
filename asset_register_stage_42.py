# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: AssetRegister
import sys

if sys.platform == "win32":
    color_support = True
    if sys.version_info >= (3, 8):
        import colorama
        colorama.init()
    else:
        color_support = False
else:
    color_support = True
