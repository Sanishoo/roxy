# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: AssetRegister
import argparse

def main():
    parser = argparse.ArgumentParser(description="AssetRegister CLI")
    parser.add_argument("--add", nargs="+", help="add asset: name owner check_date status")
    parser.add_argument("--check", nargs="+", help="check asset: name status")
    parser.add_argument("--remove", help="remove asset by name")
    parser.add_argument("--list", action="store_true", help="list all assets")
    args = parser.parse_args()
    if args.add:
        name, owner, check_date, status = args.add
        register.add_asset(name, owner, check_date, status)
        print(f"Added {name}")
    elif args.check:
        name, new_status = args.check
        register.check_asset(name, new_status)
        print(f"Checked {name}: {new_status}")
    elif args.remove:
        register.remove_asset(args.remove)
        print(f"Removed {args.remove}")
    elif args.list:
        register.list_assets()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
