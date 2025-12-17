# 📘 Judul Proyek
*Prediksi Harga Mobil Menggunakan Machine Learning dan Deep Learning*

## 👤 Informasi
- **Nama:** [Fajar Hakiki]  
- **Repo:** [https://github.com/Fajarhakiki/DataScience.git]  
- **Video:** [...]  

---

# 1. 🎯 Ringkasan Proyek
- Menyelesaikan permasalahan sesuai domain  
- Melakukan data preparation  
- Membangun 3 model: **Baseline**, **Advanced**, **Deep Learning**  
- Melakukan evaluasi dan menentukan model terbaik  

---

# 2. 📄 Problem & Goals
**Problem Statements:**  
- [Dataset memiliki missing values yang signifikan (normalized-losses 20%, bore/stroke/horsepower 1-2%).]  
- [Terdapat outliers pada harga mobil premium (>$35,000) yang perlu di-handle dengan tepat.]
- [Hubungan antara fitur dan harga tidak sepenuhnya linear, memerlukan model non-linear.]
- [Diperlukan model yang dapat memprediksi harga dengan error minimal untuk keputusan bisnis.]  

**Goals:**  
- [Membangun model prediksi harga dengan R² Score > 0.80 dan RMSE < $3,500.]  
- [Menggunakan 15 fitur numerik terpenting dari total 25 fitur untuk menghindari overfitting.]
- [Membandingkan performa model linear, ensemble, dan neural network pada data tabular.]
- [Mengidentifikasi fitur terpenting yang mempengaruhi harga mobil untuk insight bisnis.]  

---
## 📁 Struktur Folder
```
project/
│
├── data/                   
│   └── imports-85.data 
    └── imports-85.names    
├── notebooks/              
│   └── 234311039_Fajar Hakiki_UAS.ipynb
│
├── src/                    
│   └── Data overview.txt
    └── Data Prepocessing.py
    └── Import Libraries.py
    └── Load data.py
    └── Model.py
    └── Perbandingan Model.py
    └── Train test.py
    └── Visualisasi Training History.py
    └── Visualisasi.py
├── models/                 
│   ├── deep_learning_model.h5
│   ├── linear_regression_model.pkl
│   └── random_forest_model.pkl
│
├── images/                
│   └── Distribusi Mobil.png
    └── Eval Metric Comparison.png
    └── Heatmap.png
    └── Korelasi.png
    └── Scatterplot Hubungan Engine Size dengan Harga.png
    └── Training Val Loss.png
│
├── .gitignore
├── Checklist Submit Proyek.md
├── Data Science_Laporan.pdf
├── LICENSE
└── README.md
├── requirements.txt
```
---

# 3. 📊 Dataset
- **Sumber:** [ UCI Machine Learning Repository (ID: 10 - Automobile)]  
- **Jumlah Data:** [205 Baris, 26 Kolom (25 features + 1 target)]  
- **Tipe:** [Tabular (Data mobil dari Ward's Automotive Yearbook 1985)]  

### Fitur Utama
| Fitur | Deskripsi |
|------|-----------|
| symboling | Risk rating (-3 safe, +3 risky) |
| engine-size | Ukuran mesin (cubic inches) |
| curb-weight | Berat kosong mobil (lbs) |
| horsepower | Tenaga kuda |
| city-mpg | Konsumsi BBM kota (mpg) |
| highway-mpg | Konsumsi BBM highway (mpg) |
| price | Harga mobil (USD) |

---

# 4. 🔧 Data Preparation
- Cleaning (Drop baris dengan missing values pada target (price) - 4 baris dihapus.)  
- Transformasi (Memilih 15 fitur numerik terpenting: symboling, normalized-losses, wheel-base, length, width, height, curb-weight, engine-size, bore, stroke, compression-ratio, horsepower, peak-rpm, city-mpg, highway-mpg.)
- Transformasi (Scaling: StandardScaler (Z-score normalization) - mean=0, std=1.)  
- Splitting (Validation split 20% dari training data untuk Deep Learning monitoring.)  

---

# 5. 🤖 Modeling
- **Model 1 – Baseline: Linear Regression [Model linear sederhana untuk regression, meminimalkan Sum of Squared Residuals.]  
- **Model 2 – Advanced ML: Random Forest Regressor [Ensemble dari Decision Trees menggunakan bagging dan random feature selection.]  
- **Model 3 – Deep Learning: Multilayer Perceptron (MLP) [Arsitektur:
Input Layer: 15 neurons (sesuai jumlah fitur)
Dense Layer 1: 64 neurons, aktivasi ReLU
Dropout: 0.2 (mencegah overfitting)
Dense Layer 2: 32 neurons, aktivasi ReLU
Dropout: 0.2
Dense Layer 3: 16 neurons, aktivasi ReLU
Output Layer: 1 neuron, aktivasi Linear (regression)]  

---

# 6. 🧪 Evaluation
**Metrik:** RMSE (Root Mean Squared Error): Rata-rata magnitude error dalam dollar.
            R² Score: Seberapa baik model menjelaskan variance (0-1, higher is better).
            MAE (Mean Absolute Error): Rata-rata absolute error, robust terhadap outliers.

### Hasil Singkat
| Model | Test RMSE | Test R² | Test MAE | Catatan |
|-------|--------|---------|---------|---------|
| Baseline | $2,342.05 |0.578 |$1,857.26 |Performa moderate |
| Advanced | $1,696.53 |0.779 |$1,186.26 |TERBAIK |
| Deep Learning | $7,111.02 |-2.888 |$6,633.25 |Overfitting parah |

---

# 7. 🏁 Kesimpulan
- Model terbaik: [Random Forest Regressor]  
- Alasan: [RMSE terendah ($1,696.53) - prediksi paling akurat,R² tertinggi (0.779) - menjelaskan 78% variance harga,Balance antara,akurasi dan generalisasi,Tidak overfitting seperti Deep Learning,Memberikan feature importance untuk business insight] 
- Insight penting: [Dataset kecil (160 samples) sangat mempengaruhi performa Deep Learning. Model dengan 3,649 parameters terlalu kompleks untuk data ini, menyebabkan severe overfitting.
Random Forest lebih cocok untuk dataset kecil karena robust dan tidak memerlukan data banyak seperti neural network.]  

---

# 8. 🔮 Future Work
- [ ] Tambah data  
- [ ] Tuning model  
- [ ] Coba arsitektur DL lain  
- [ ] Deployment  

---

# 9. 🔁 Reproducibility
Gunakan environment:
