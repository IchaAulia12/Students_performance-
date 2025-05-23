# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal dengan reputasi lulusan yang baik. Namun, dalam beberapa tahun terakhir, jumlah mahasiswa yang tidak menyelesaikan studi atau dropout semakin meningkat. Tingginya angka dropout menjadi tantangan besar karena berdampak pada citra institusi, efisiensi operasional, dan akreditasi institusi itu sendiri. Oleh karena itu, penting bagi pihak institusi untuk memahami pola dan faktor-faktor penyebab dropout, serta membangun sistem prediktif agar dapat melakukan intervensi lebih dini.

### Permasalahan Bisnis
- Tingginya angka dropout mahasiswa dari Jaya Jaya Institut.
- Kurangnya pemahaman tentang faktor-faktor utama yang memengaruhi dropout.
- Tidak adanya sistem monitoring performa mahasiswa secara menyeluruh.
- Belum adanya sistem prediksi mahasiswa yang berisiko dropout.

### Cakupan Proyek
- Melakukan eksplorasi data (EDA) untuk memahami karakteristik mahasiswa dan hubungan antar fitur dengan status kelulusan.
- Menganalisis berbagai faktor yang berpotensi memengaruhi dropout, seperti status pernikahan, program studi, jenis kehadiran, nilai akademik, kondisi ekonomi, beasiswa, usia, jenis kelamin, dan jumlah mata kuliah.
- Membangun dashboard untuk monitoring performa mahasiswa secara visual.
- Mengembangkan sistem machine learning untuk memprediksi kemungkinan dropout mahasiswa berdasarkan data historis.

### Persiapan

[**Sumber data:**](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) Dataset "students' performance" dari pihak Jaya Jaya Institut.

Setup environment:

```
Tools yang digunakan:
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit)
- Looker Studio (untuk visualisasi dashboard)
- Jupyter Notebook (untuk eksplorasi dan modelling)
```
## Setup menggunakan Google colab 
```
!pip install -r requirements.txt
```
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup dengan pipenv (alternatif)
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install --python 3.9
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run app.py
```

## Business Dashboard

Dashboard yang dibangun menyajikan visualisasi interaktif terkait performa mahasiswa, faktor-faktor yang berkontribusi terhadap dropout, dan status akhir mahasiswa berdasarkan berbagai kategori seperti program studi, jenis kehadiran, beasiswa, dan lainnya. Dashboard ini membantu manajemen dalam mengambil keputusan strategis berbasis data.

Beberapa visualisasi utama yang ditampilkan dalam dashboard meliputi:
- **Distribusi status akhir mahasiswa** (lulus, dropout, masih aktif)
- **Performa akademik** berdasarkan program studi, rata-rata nilai semester, serta status beasiswa.
- **Karakteristik demografis** mahasiswa yang dropout, termasuk status pernikahan dan kelompok usia.
- **Analisis pola kehadiran** (daytime vs evening), yang memperlihatkan tren dropout pada kelas malam.

Dashboard ini menjadi alat bantu strategis bagi pihak manajemen akademik untuk:

- Mengidentifikasi kelompok mahasiswa yang berisiko tinggi mengalami dropout.
- Memahami korelasi antara faktor-faktor tertentu (misalnya beasiswa atau program studi) dengan hasil akhir studi mahasiswa.
- Membantu pengambilan keputusan berbasis data untuk perencanaan intervensi dini dan pengembangan kebijakan pendidikan.

![image](https://github.com/user-attachments/assets/0b6ebf27-c7b1-4f2d-88a0-0fd62ed18c90)
![image](https://github.com/user-attachments/assets/7fa8105c-e8c4-4b29-9ae6-f1dda40d7853)


🔗 [**Link Dashboard:**](https://lookerstudio.google.com/reporting/26aff7e5-df6e-4767-85ac-b9521b292c2f/page/1gQLF)

## Menjalankan Sistem Machine Learning

Sistem machine learning yang dikembangkan dapat memprediksi kemungkinan seorang mahasiswa akan dropout atau lulus berdasarkan fitur-fitur akademik dan demografis.

![image](https://github.com/user-attachments/assets/98f08982-43a0-4b3b-b679-0f6956e99c4d)

sistem akan menampilkan hasil prediksi dengan tiga output sebagai berikut :

**1. Dropout**

![image](https://github.com/user-attachments/assets/48dd6e00-f679-4093-8d02-3b8c9cedb2a0)

**2. Enrolled**

![Screenshot 2025-05-22 091651](https://github.com/user-attachments/assets/958c591d-a50b-4617-86e1-69f42b6285bc)

**3. Graduate**

![Screenshot 2025-05-22 091530](https://github.com/user-attachments/assets/fbbd4437-d318-4e2a-ac72-307e9e12b802)


```bash
Langkah-langkah menjalankan prototipe:
1. Jalankan script Streamlit dengan perintah:
   $ streamlit run app.py
2. Masukkan data mahasiswa melalui form input.
3. Model akan menampilkan hasil prediksi status mahasiswa.
4. Backend model diload dari file pickle/joblib hasil training.
```

🔗 [**Link Prototype:**](https://studentpredict.streamlit.app/)

## Conclusion

Hasil analisis menunjukkan bahwa tingginya tingkat dropout mahasiswa di Jaya Jaya Institut dipengaruhi oleh berbagai faktor yang saling terkait. Beberapa temuan penting meliputi:

- Mahasiswa dengan nilai akademik rendah dan status non-beasiswa memiliki proporsi dropout tertinggi.

- Program studi tertentu seperti Basic Education dan Equine Culture mencatat angka dropout yang relatif lebih tinggi dibandingkan jurusan lainnya.

- Mahasiswa kelas malam (evening class) cenderung lebih berisiko mengalami dropout dibandingkan kelas reguler (daytime).

- Mahasiswa berusia muda dan belum menikah mendominasi kelompok yang mengalami dropout, menunjukkan perlunya pendekatan personal dan dukungan akademik tambahan untuk kelompok ini.

Sistem prediktif yang dikembangkan melalui model machine learning mampu mengidentifikasi mahasiswa dengan risiko tinggi untuk tidak menyelesaikan studi. Hal ini memberikan peluang bagi institusi untuk melakukan intervensi tepat waktu, baik melalui bimbingan akademik, konseling psikologis, maupun dukungan finansial tambahan.

### Rekomendasi Action Items

1. **Penerapan sistem prediksi dropout berbasis data**  
   Jaya Jaya Institut perlu mengintegrasikan sistem prediksi ini ke dalam sistem akademik mereka. Prosesnya bisa berupa evaluasi rutin setiap awal semester dengan data mahasiswa terbaru, dan hasilnya akan digunakan untuk menandai mahasiswa dengan potensi dropout tinggi.

2. **Pembentukan tim intervensi akademik dan psikologis**  
   Mahasiswa yang masuk dalam kategori risiko tinggi dari hasil prediksi perlu segera dihubungi oleh tim khusus yang terdiri dari dosen wali, konselor akademik, dan psikolog. Tim ini akan bertugas memberikan pendampingan personal dan strategi belajar yang lebih terarah.

3. **Evaluasi kurikulum dan beban studi pada program studi bermasalah**  
   Program seperti Basic Education dan Equinculture yang memiliki angka dropout tinggi perlu dilakukan evaluasi. Ini bisa mencakup survei kepuasan mahasiswa, kesulitan kurikulum, atau ketersediaan fasilitas pendukung. Jika perlu, dilakukan penyusunan ulang silabus agar lebih proporsional.

4. **Optimalisasi jadwal kelas malam dan pembelajaran fleksibel**  
   Mahasiswa kelas malam menunjukkan dropout lebih tinggi. Institusi dapat mempertimbangkan implementasi blended learning atau menyediakan kelas tambahan di akhir pekan untuk meringankan beban belajar sambil bekerja.

5. **Monitoring performa beasiswa secara berkala**  
   Untuk memastikan efektivitas program beasiswa, perlu ada pelaporan rutin dari penerima beasiswa terkait capaian akademik mereka. Mahasiswa yang mendapatkan beasiswa namun menunjukkan performa buruk dapat diberikan bimbingan intensif agar tidak mengalami dropout.

6. **Penyusunan modul pembelajaran tambahan bagi mahasiswa tahun pertama**  
   Karena nilai akademik di semester 1 dan 2 sangat berpengaruh terhadap kelulusan, maka Jaya Jaya Institut bisa menyediakan modul bimbingan belajar atau remedial learning online sebagai bentuk intervensi awal untuk mahasiswa baru.
