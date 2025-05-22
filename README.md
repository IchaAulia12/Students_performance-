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

**Sumber data:** Dataset "students' performance" dari pihak Jaya Jaya Institut.

**Setup environment:**
```bash
Python 3.10
Jupyter Notebook
Pandas
Numpy
Matplotlib
Seaborn
Scikit-learn
Streamlit
joblib
```

## Business Dashboard

Dashboard yang dibangun menyajikan visualisasi interaktif terkait performa mahasiswa, faktor-faktor yang berkontribusi terhadap dropout, dan status akhir mahasiswa berdasarkan berbagai kategori seperti program studi, jenis kehadiran, beasiswa, dan lainnya. Dashboard ini membantu manajemen dalam mengambil keputusan strategis berbasis data.

🔗 **Link Dashboard:** (Akan disediakan setelah deploy)

## Menjalankan Sistem Machine Learning

Sistem machine learning yang dikembangkan dapat memprediksi kemungkinan seorang mahasiswa akan dropout atau lulus berdasarkan fitur-fitur akademik dan demografis.

```bash
Langkah-langkah menjalankan prototipe:
1. Jalankan script Streamlit dengan perintah:
   $ streamlit run app.py
2. Masukkan data mahasiswa melalui form input.
3. Model akan menampilkan hasil prediksi status mahasiswa.
4. Backend model diload dari file pickle/joblib hasil training.
```

🔗 **Link Prototype:** (Akan disediakan setelah deploy)

## Conclusion

Proyek ini berhasil mengidentifikasi sejumlah faktor utama yang berkontribusi terhadap kemungkinan dropout mahasiswa. Model prediksi yang dibangun memiliki potensi untuk digunakan sebagai sistem pendukung keputusan dalam proses bimbingan mahasiswa berisiko tinggi. Selain itu, dashboard interaktif memungkinkan pihak manajemen untuk memantau performa mahasiswa secara lebih efektif.

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
