# Laporan Praktikum: Analisis Performa Penjualan E-commerce

## 1. Business Question
[cite_start]Analisis ini bertujuan untuk menjawab beberapa pertanyaan kunci bisnis berikut[cite: 65, 83]:
* [cite_start]**Tren Penjualan:** Bagaimana fluktuasi total penjualan dalam rentang waktu bulanan? [cite: 66]
* [cite_start]**Korelasi Pemasaran:** Apakah anggaran iklan (`Ad_Budget`) memiliki korelasi kuat terhadap total penjualan? [cite: 77]
* [cite_start]**Identifikasi Produk:** Produk mana yang termasuk kategori *underperformer* (harga tinggi namun volume penjualan rendah)? [cite: 89, 90]
* [cite_start]**Segmentasi Pelanggan:** Siapa pelanggan yang masuk dalam segmen prioritas untuk program loyalitas (RFM)? [cite: 97, 102]
* [cite_start]**Efisiensi Kategori:** Seberapa efisien alokasi anggaran iklan pada setiap kategori produk? [cite: 104, 105]

## 2. Data Wrangling
Proses pembersihan dan persiapan data dilakukan untuk memastikan akurasi analisis:
* [cite_start]**Pembersihan Data:** Menghapus baris dengan harga unit (`Price_Per_Unit`) yang tidak valid atau di bawah 0[cite: 62].
* [cite_start]**Konversi Tipe Data:** Mengubah kolom `Order_Date` menjadi format *datetime* agar bisa diproses secara temporal[cite: 63].
* [cite_start]**Feature Engineering:** Membuat kolom baru `Month` untuk analisis tren bulanan[cite: 69].

## 3. Insights & Visualizations

### A. Tren Penjualan Bulanan
[cite_start]Visualisasi menggunakan *Line Chart* menunjukkan fluktuasi pendapatan dari waktu ke waktu untuk mengidentifikasi pola pertumbuhan bulanan perusahaan[cite: 66, 73].

![Tren Penjualan Bulanan](AnalisisTrenPenjualanBulanan%28Line%20Chart%29.png)

### B. Analisis Korelasi (Heatmap)
[cite_start]Berdasarkan *Heatmap*, kita melihat hubungan antara `Total_Sales`, `Ad_Budget`, dan variabel lainnya untuk mengukur efektivitas biaya iklan[cite: 76, 81].

![Analisis Korelasi](AnalisisKorelasi%28Heatmap%29.png)

### C. Produk "Underperformer"
[cite_start]Melalui *Scatter Plot*, ditemukan produk yang memiliki harga di atas rata-rata namun volume kuantitas rendah, yang berpotensi membebani arus kas[cite: 92, 93, 96].

![Identifikasi Produk Underperformer](IdentifikasiProdukUnderperformer.png)

### D. Segmentasi Pelanggan (RFM Analysis)
[cite_start]Pelanggan dikelompokkan berdasarkan *Recency*, *Frequency*, dan *Monetary* untuk menentukan strategi pemasaran yang lebih terarah[cite: 115, 116].

![Segmentasi Pelanggan](SegmentasiPelanggan%28RFM%20Analysis%29.png)

## 4. Uji Hipotesis Sederhana
[cite_start]Dilakukan pengujian pengaruh iklan dengan membagi data menjadi dua kelompok berdasarkan nilai median anggaran iklan[cite: 109, 110]:
* **Iklan Tinggi vs Iklan Rendah:** Membandingkan rata-rata penjualan dari kedua kelompok tersebut.
* **Hasil:** Analisis menunjukkan apakah peningkatan `Ad_Budget` benar-benar menghasilkan peningkatan `Total_Sales` yang signifikan.

## 5. Recommendation
1. [cite_start]**Strategi Harga:** Melakukan evaluasi harga atau memberikan promo pada produk *underperformer* agar stok lebih cepat laku[cite: 152].
2. [cite_start]**Re-alokasi Budget:** Mengalihkan anggaran iklan ke kategori produk yang memiliki rasio efisiensi lebih tinggi[cite: 106].
3. [cite_start]**Loyalty Program:** Memprioritaskan segmen pelanggan dengan skor RFM tinggi untuk menjaga retensi pelanggan[cite: 102].

---
*Laporan ini disusun sebagai bagian dari tugas Praktikum Analisis dan Visualisasi Data.*
