# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech sangat bergantung pada sumber daya manusia (SDM) yang berkualitas tinggi, seperti pengajar, pengembang kurikulum, hingga talenta teknologi (Software Engineer/Data Scientist) untuk memberikan layanan pendidikan terbaik. Tingginya tingkat perputaran karyawan (*employee turnover/attrition*) dapat mengganggu kelancaran operasional perusahaan, menurunkan kualitas produk pembelajaran, serta memicu lonjakan biaya untuk proses rekrutmen dan *onboarding* karyawan baru. Mempertahankan talenta terbaik adalah kunci krusial untuk menjaga stabilitas dan pertumbuhan bisnis perusahaan Edutech di pasar yang kompetitif.

## Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang diselesaikan melalui proyek ini:
1. **Membengkaknya Biaya Operasional HR:** Kerugian waktu dan finansial yang signifikan akibat keluarnya karyawan secara tidak terduga.
2. **Ketiadaan Sistem Peringatan Dini (*Early Warning System*):** Departemen HR kesulitan mendeteksi karyawan mana yang memiliki indikasi atau probabilitas tinggi untuk mengundurkan diri (*resign*) dalam waktu dekat.
3. **Inefisiensi Program Retensi:** Program retensi karyawan (seperti bonus, kenaikan gaji, atau konseling) menjadi kurang efektif dan boros anggaran karena tidak disasarkan secara spesifik pada karyawan yang benar-benar berisiko keluar.

## Cakupan Proyek
Proyek ini mencakup beberapa tahapan utama:
1. **Eksplorasi & Prapemrosesan Data (EDA):** Menganalisis karakteristik data HR dan mengidentifikasi masalah ketidakseimbangan kelas (*imbalanced data*).
2. **Pemodelan Machine Learning:** Melatih dan mengevaluasi empat algoritma klasifikasi (Logistic Regression, Random Forest, XGBoost, dan SVM) untuk memprediksi target `Attrition`.
3. **Evaluasi Berbasis Kelas Minoritas:** Membandingkan performa model menggunakan metrik *Precision*, *Recall*, dan *F1-Score*, bukan sekadar *Accuracy*, mengingat sifat data yang tidak seimbang.
4. **Pengembangan Business Dashboard:** Membangun *dashboard* interaktif menggunakan Streamlit untuk memvisualisasikan temuan analitik dan perbandingan performa model bagi para pemangku kepentingan.

## Persiapan
**Sumber data:** 
Dataset HR Analytics Perusahaan (format CSV) yang mencakup data demografi, riwayat pekerjaan, dan status *attrition* karyawan. Dataset pengujian terdiri dari 212 baris data uji, dengan rasio kelas yang sangat tidak seimbang (173 Retained vs 39 Attrition).

**Setup environment:**
Untuk menjalankan proyek ini secara lokal, pastikan Python sudah terinstal, lalu jalankan perintah berikut di terminal:

```bash
# Clone repositori ini
git clone [https://github.com/rianarifiya/submission-penerapan-data-science.git](https://github.com/rianarifiya/submission-penerapan-data-science.git)
cd submission-penerapan-data-science

# Instalasi library yang dibutuhkan
pip install -r requirements.txt
```

## Business Dashboard
Business Dashboard dirancang khusus untuk audiens profesional (Departemen HR dan Manajemen Eksekutif) menggunakan Streamlit dengan pendekatan antarmuka yang bersih (clean) dan minimalis. Dashboard ini menyajikan:

- Executive Summary: Menampilkan metrik utama seperti Total Data Uji, Attrition Rate, dan nilai performa model terbaik.

- Visualisasi Distribusi Kelas: Donut chart interaktif yang menyoroti masalah imbalanced data antara karyawan yang bertahan dan keluar.

- Komparasi Model Prediktif: Grouped bar chart dan tabel metrik yang membandingkan performa Logistic Regression, Random Forest, XGBoost, dan SVM berdampingan secara detail, difokuskan pada kemampuan pendeteksian kelas minoritas (Attrition).

Link Dashboard:
(Tambahkan link Streamlit Cloud di sini jika sudah berhasil di-deploy)

Untuk menjalankan dashboard secara lokal:

```Bash
streamlit run dashboard_submission.py
```

## Conclusion
Berdasarkan eksperimen pemodelan Machine Learning yang telah dilakukan, dapat ditarik konklusi sebagai berikut:

1. Kondisi dataset sangat tidak seimbang (173 kelas Retained berbanding 39 kelas Attrition).

2. Logistic Regression terpilih sebagai model prediktif terbaik di antara model lainnya karena memberikan keseimbangan paling optimal dengan F1-Score tertinggi (0.3265) untuk memprediksi kelas minoritas.

3. Model Logistic Regression memiliki tingkat Precision sebesar 80.0%. Artinya, jika model memprediksi seorang karyawan akan keluar, akurasi tebakan tersebut sangat tinggi (8 dari 10 prediksi adalah benar), sehingga tingkat false positive sangat minim.

4. Meskipun memiliki Precision yang sangat baik, kelemahan seluruh model saat ini berada pada tingkat Recall (20.5%) yang masih rendah. Hal ini menandakan model masih kesulitan mendeteksi seluruh populasi karyawan yang berpotensi resign akibat kurangnya representasi sampel data minoritas.

## Rekomendasi Action Items
Berangkat dari konklusi di atas, berikut adalah rekomendasi tindakan yang dapat diambil perusahaan guna menyelesaikan permasalahan bisnis:

- Action Item 1: Terapkan Intervensi Retensi yang Tepat Sasaran
Departemen HR harus segera menggunakan hasil prediksi Logistic Regression untuk melakukan intervensi (seperti sesi konseling 1-on-1 atau negosiasi insentif) kepada karyawan yang telah diidentifikasi berisiko tinggi. Dengan tingkat Precision 80%, alokasi waktu dan dana retensi ini akan menjadi sangat efisien dan meminimalisir salah sasaran.

- Action Item 2: Optimalisasi Model dengan Pendekatan Imbalanced Learning
Tim Data/IT perlu melakukan iterasi model lanjutan dengan menerapkan teknik penyeimbangan data pada tahap prapemrosesan (misalnya menggunakan SMOTE untuk menciptakan data sintetis kelas minoritas) atau menambahkan class weight pada parameter model. Hal ini diwajibkan untuk menaikkan nilai Recall sehingga tidak ada lagi karyawan potensial keluar yang luput dari pendeteksian sistem (false negative

