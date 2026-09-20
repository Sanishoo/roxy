# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: AssetRegister
import csv, json

def load_records(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def save_records(records, path):
    with open(path, 'w', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r) + '\n')

def load_csv(path):
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict((k.strip(), v.strip()) for k, v in row.items()))
    return rows

def save_csv(records, path):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'status', 'owner', 'check_date', 'history'])
        writer.writeheader()
        writer.writerows(records)

if __name__ == '__main__':
    print('Загрузка JSON:')
    recs = load_records('assets.json')
    print(recs[:2])
    print('Загрузка CSV:')
    csv_recs = load_csv('assets.csv')
    print(csv_recs[:2])
