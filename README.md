# 🌍 Inflation Dataset and Analysis Scripts

This folder contains **annual inflation data for countries**, related **meta information** (country, region, flag), and the **Python scripts** used to work with this data. The files are organized to be easily used in platforms like [**Flourish**](https://flourish.studio/) for visualization purposes.

---

## 📁 Files

### `1. annual_with_meta.csv`

- 📌 **Each row represents a country.**
- 📄 **Columns:**
  - `Entity_Mapped`: Country name
  - `Region`: Geographic region
  - `Image URL`: Flag (SVG image URL)
  - `1960 - 2023`: Years (empty values used as placeholders)
- 🎯 **Use case:** Template creation and visual tests (e.g., Flag Race)

---

### `2. annual_meta_with_inflation.csv`

- 🔗 Combined from `annual_with_meta.csv` and `inflation-of-consumer-prices.csv`
- 📄 **Columns:**
  - `Entity_Mapped`, `Region`, `Image URL`
  - `1960 - 2023`: Annual inflation values (blank if missing)
- 📊 **Use case:** Enriched data for time-series visualizations and flag-integrated analysis

---

### `3. inflation-of-consumer-prices.csv`

- 🧪 **Raw data source.**
- 📄 **Columns:**
  - `Entity` – Country name
  - `Code` – ISO country code
  - `Year` – Year
  - `Inflation, consumer prices (annual %)` – Annual inflation rate
- 📈 **Use case:** Pivot to reshape for year-based or country-based analysis

---

### `4. annual_meta_with_inflation.py`

- 🛠️ **What it does:**
  - Merges inflation data into `annual_with_meta.csv` and generates `annual_meta_with_inflation.csv`
- 🚀 **Run with:**
  ```bash
  python annual_meta_with_inflation.py
  ```
- ✅ Outputs clean and ready-to-use data for Flourish

---

## 📌 Flourish Usage Notes

| Column          | Purpose                          |
| --------------- | -------------------------------- |
| `Entity_Mapped` | Country name (used as label)     |
| `Region`        | Grouping by region               |
| `Image URL`     | Country flag (SVG image URL)     |
| `1960 - 2023`   | Time-series and animation values |

---

## 🏁 Flag Race Example (With SVG Flags)

> A placeholder area below is reserved for a Flag Race chart created in Flourish:

📝 **Note:** Use `annual_meta_with_inflation.csv` for visualization.

---

## 📚 How to Use

1. **Load the dataset:** Upload `annual_meta_with_inflation.csv` to Flourish.
2. **Map the columns:**
   - X-axis: Any year (e.g., `2000`)
   - Group by: `Region` or `Entity_Mapped`
   - Image: `Image URL` (flag)
3. **Choose a chart type:**
   - Line Chart, Heatmap, Bar Chart Race, etc.

---

## 📃 License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).\
Feel free to use, modify, and share it.

---

# 🌍 Enflasyon Veri Seti ve Analiz Scriptleri

Bu klasör, **ülkelerin yıllık enflasyon verilerini**, ilgili **meta bilgileri** (ülke, bölge, bayrak) ve bu verilerle çalışan **Python scriptlerini** içerir. Veriler, özellikle [**Flourish**](https://flourish.studio/) gibi görselleştirme platformlarında kolayca kullanılabilecek şekilde düzenlenmiştir.

---

## 📁 Dosyalar

### `1. annual_with_meta.csv`

- 📌 **Her satır bir ülkeye aittir.**
- 📄 **Sütunlar:**
  - `Entity_Mapped`: Ülke adı
  - `Region`: Bölge adı
  - `Image URL`: Ülke bayrağı (SVG bağlantısı)
  - `1960 - 2023`: Yıllar (veriler boş; yer tutucu olarak kullanılabilir)
- 🎯 **Kullanım amacı:** Görsel testler, şablon oluşturma (Flag Race gibi)

---

### `2. annual_meta_with_inflation.csv`

- 🔗 `annual_with_meta.csv` + `inflation-of-consumer-prices.csv` birleşimidir.
- 📄 **Sütunlar:**
  - `Entity_Mapped`, `Region`, `Image URL`
  - `1960 - 2023`: Yıllık enflasyon verileri (boş hücre = eksik veri)
- 📊 **Kullanım amacı:** Zenginleştirilmiş zaman serisi analizi ve bayraklı görselleştirme

---

### `3. inflation-of-consumer-prices.csv`

- 🧪 **Ham veri seti.**
- 📄 **Sütunlar:**
  - `Entity` – Ülke adı
  - `Code` – ISO ülke kodu
  - `Year` – Yıl
  - `Inflation, consumer prices (annual %)` – Yıllık enflasyon oranı
- 📈 **Kullanım amacı:** Pivot tablo oluşturarak yıllık bazda analiz

---

### `4. annual_meta_with_inflation.py`

- 🛠️ **Ne yapar?**
  - `annual_with_meta.csv` dosyasına enflasyon verilerini ekleyerek `annual_meta_with_inflation.csv` dosyasını üretir.
- 🚀 **Çalıştır:**
  ```bash
  python annual_meta_with_inflation.py
  ```
- ✅ Flourish için temiz ve hazır veri üretir.

---

## 📌 Flourish Kullanım Notları

| Sütun           | Amaç                                |
| --------------- | ----------------------------------- |
| `Entity_Mapped` | Ülke adı (etiket olarak kullanılır) |
| `Region`        | Bölgeye göre gruplama               |
| `Image URL`     | Ülke bayrağı (SVG, doğrudan görsel) |
| `1960 - 2023`   | Zaman serisi analizi, animasyonlar  |

---

## 🏁 Flag Race Örneği (SVG Bayraklarla)

> Aşağıda Flourish kullanılarak oluşturulmuş bir Flag Race (Bayrak Yarışı) görseli için boşluk bırakılmıştır:

📝 **Not:** Görselleştirme için `annual_meta_with_inflation.csv` dosyasını kullanınız.

---

## 📚 Kullanım Adımları

1. **Veriyi inceleyin:**\
   `annual_meta_with_inflation.csv` dosyasını Flourish'e yükleyin.
2. **Sütunları eşleştirin:**
   - X ekseni: `Yıllar ("2000" gibi)`
   - Gruplama: `Region` veya `Entity_Mapped`
   - Görsel: `Image URL` (bayrak)
3. **Görselleştirme türü seçin:**
   - Line Chart, Heatmap, Bar Chart Race vb.

---

## 📃 Lisans

Bu proje [MIT Lisansı](https://opensource.org/license/mit/) ile lisanslanmıştır.\
Özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.

