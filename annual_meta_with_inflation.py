import csv
from collections import defaultdict

# Yıl aralığı
years = [str(y) for y in range(1960, 2024)]

# 1. Enflasyon verisini oku: (ülke, yıl) -> enflasyon
inflation = defaultdict(dict)
with open("inflation-of-consumer-prices.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row["Entity"].strip()
        year = str(row["Year"]).strip()
        value = row["Inflation, consumer prices (annual %)"]
        if country and year:
            inflation[country][year] = value

# 2. annual_with_meta.csv dosyasını oku ve yeni dosyayı oluştur
with open("annual_with_meta.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0][:3] + years

with open("annual_meta_with_inflation.csv", "w", newline='', encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(header)
    for row in rows[1:]:
        country = row[0].strip()
        meta = row[:3]
        infl_row = [inflation.get(country, {}).get(y, "") for y in years]
        writer.writerow(meta + infl_row) 