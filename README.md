# 👥 HR Attrition Analytics & Prediction

Proyek ini bertujuan untuk membangun model *Machine Learning* yang dapat memprediksi potensi keluarnya karyawan (*Employee Attrition*). Solusi ini dirancang untuk membantu Departemen HR dalam mengambil langkah preventif guna mempertahankan talenta terbaik perusahaan.

## 📌 Latar Belakang Masalah
Perputaran karyawan (*turnover*) yang tinggi memakan biaya besar bagi perusahaan, baik dari segi rekrutmen maupun pelatihan ulang. Departemen HR menghadapi tantangan untuk:
1. Mengetahui siapa saja karyawan yang memiliki probabilitas tinggi untuk *resign* (Attrition = 1).
2. Memiliki alat pendukung keputusan yang berbasis data untuk melakukan intervensi dini.

## 🛠️ Metodologi & Eksperimen Model
Dataset HR yang digunakan memiliki karakteristik **sangat tidak seimbang (imbalanced)**, di mana mayoritas karyawan bertahan (173 orang / Kelas 0) dan minoritas yang keluar (39 orang / Kelas 1). 

Empat algoritma klasifikasi telah dievaluasi:
* Logistic Regression
* Random Forest
* XGBoost
* Support Vector Machine (SVM)

## Conclusion
Proyek ini bertujuan untuk memahami faktor-faktor yang mempengaruhi tingkat attrition (keluar) karyawan dari perusahaan Jaya Jaya Maju dan membangun model prediktif untuk mengidentifikasi karyawan dengan risiko keluar tinggi. Berikut ini adalah temuan-temuan utama dan insight yang diperoleh:

# 1. Faktor-faktor Penyebab Attrition
Berdasarkan analisis data dan model prediktif, berikut adalah faktor utama yang mempengaruhi attrition:
1. `OverTime`
- Karyawan yang sering lembur (OverTime = Yes) memiliki risiko keluar yang jauh lebih tinggi dibandingkan dengan yang tidak lembur.
- Fitur ini adalah prediktor terkuat dalam model prediktif.
2. `MonthlyIncome`
- Pendapatan yang lebih rendah meningkatkan risiko keluar karyawan.
- Fitur ini mencerminkan pentingnya kepuasan finansial dalam retensi karyawan.
3. `YearsAtCompany` dan `TotalWorkingYears`
- Masa kerja pendek baik di perusahaan maupun secara total adalah indikator risiko tinggi.
4. Fitur pendukung lain
- Fitur seperti `DistanceFromHome` dan `Age` memiliki kontribusi kecil, tetapi tetap relevan dalam memahami pola attrition.

# 2. Model Prediktif Terbaik
Model terbaik yang digunakan dalam proyek ini adalah Random Forest dengan metrik performa sebagai berikut:
- Accuracy: 84%
- Precision: 85%
- Recall: 99%
- F1-Score: 91%
  
# 3. Feature Importance
Dari analisis feature importance menggunakan model Random Forest, didaparkan bahwa:
- `TotalWorkingYears` adalah fitur dengan kontribusi terbesar terhadap prediksi.
- `YearsAtCompany` dan `Age` juga memiliki peran penting.

## Jawaban terhadap Pertanyaan Bisnis
1. Apa faktor utama yang memengaruhi attrition?
- Faktor utama adalah OverTime, MonthlyIncome, dan YearsAtCompany.
2. Bagaimana tingkat kepuasan karyawan memengaruhi attrition?
- Fitur seperti JobSatisfaction tidak signifikan dalam model prediktif, tetapi tetap relevan secara deskriptif.
3. Apa pola perilaku karyawan dengan risiko keluar tinggi?
- Karyawan yang lembur berlebihan, memiliki pendapatan rendah, dan masa kerja pendek cenderung memiliki risiko tinggi.
4. Apakah kita memiliki alat bantu untuk memantau attrition?
- Model prediktif dan visualisasi hasil dapat digunakan untuk membangun dashboard interaktif untuk monitoring risiko.

## Karakteristik Umum Karyawan yang Melakukan Attrition
Berdasarkan analisis data, berikut adalah karakteristik umum karyawan yang melakukan attrition:

1. Demografis:
- Usia: Rata-rata usia karyawan yang keluar adalah 30-an tahun.
- Jenis Kelamin: Mayoritas adalah pria (Male).
- Status Pernikahan: Sebagian besar karyawan yang keluar adalah Single, diikuti oleh Married.
2. Pekerjaan dan Departemen:
- Peran Kerja: Posisi yang paling sering melakukan attrition adalah Laboratory Technician.
- Departemen: Departemen Research & Development memiliki tingkat attrition tertinggi.
3. Faktor Finansial dan Beban Kerja:
- Pendapatan: Rata-rata pendapatan bulanan karyawan yang keluar adalah 4,872.
- Lembur (OverTime): Sebagian besar karyawan yang keluar bekerja lembur secara signifikan.
4. Kepuasan dan Keseimbangan:
- Kepuasan Kerja: Rata-rata tingkat kepuasan kerja adalah 2.5 (Medium).
- Keseimbangan Kerja-Hidup: Rata-rata berada di tingkat 2.67 (Moderate).
5. Masa Kerja:
- Masa Kerja di Perusahaan: Rata-rata masa kerja adalah 5 tahun, dengan beberapa karyawan memiliki masa kerja sangat panjang hingga 40 tahun.

# Rekomendasi Action Items untuk Perusahaan
1. Kurangi Lembur Berlebihan:
Berikan program kerja fleksibel untuk meningkatkan keseimbangan kerja-hidup.
2. Kaji Skala Gaji:
Sesuaikan gaji karyawan agar kompetitif di pasar dan berikan insentif tambahan.
3. Perkuat Retensi Karyawan Baru:
Implementasikan program onboarding dan mentoring untuk karyawan dengan masa kerja pendek.
4. Mengidentifikasi karyawan dengan YearsAtCompany dan TotalWorkingYears yang pendek, lalu memberikan perhatian khusus terhadap pengembangan karier dan kepuasan mereka.
5. Menciptakan lingkungan kerja yang lebih inklusif dan mendukung bagi karyawan dari berbagai kelompok usia.
6. Gunakan Model Prediktif:
Integrasikan model Random Forest untuk memonitor risiko secara real-time melalui dashboard HR.

## 📊 Dashboard Interaktif
Proyek ini dilengkapi dengan *Business Dashboard* berbasis Streamlit.
Untuk menjalankan dashboard secara lokal:
```bash
pip install -r requirements.txt
streamlit run dashboard.py
