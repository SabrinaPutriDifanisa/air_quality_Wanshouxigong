# Air Quality Dashboard for Wanshouxigong District
# Monitoring Changes in Pollutants Over Time

Dashboard ini digunakan untuk menampilkan hasil analisis data kualitas udara di Distrik Wanshouxigong secara interaktif.

## Cara Menjalankan

1. Pastikan Python sudah terinstal di komputer Anda.
2. Instal pustaka yang diperlukan dengan perintah berikut:
   ```sh
   pip install -r requirements.txt
3. Jalankan aplikasi dengan perintah
   streamlit run dashboard.py
4. Dashboard akan terbuka secara otomatis di browser.


# Struktur Direktori
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt

#DATASET
## Dataset
Dataset ini berisi informasi kualitas udara dengan kolom-kolom sebagai berikut:

- *No*: Nomor urut.
- *year*: Tahun pengukuran.
- *month*: Bulan pengukuran.
- *day*: Hari pengukuran.
- *hour*: Jam pengukuran.
- *PM2.5*: Konsentrasi partikel halus dengan diameter kurang dari 2.5 mikrometer (µg/m³).
- *PM10*: Konsentrasi partikel dengan diameter kurang dari 10 mikrometer (µg/m³).
- *SO2*: Konsentrasi sulfur dioksida (µg/m³).
- *NO2*: Konsentrasi nitrogen dioksida (µg/m³).
- *CO*: Konsentrasi karbon monoksida (µg/m³).
- *O3*: Konsentrasi ozon (µg/m³).
- *TEMP*: Suhu (°C).
- *PRES*: Tekanan atmosfer (hPa).
- *DEWP*: Suhu titik embun (°C).
- *RAIN*: Curah hujan (mm).
- *wd*: Arah angin (derajat).
- *WSPM*: Kecepatan angin (m/s).
- *station*: Nama stasiun pengukuran.

Dataset ini digunakan untuk menganalisis kualitas udara berdasarkan data polutan dan kondisi meteorologi di distrik Wanshouxigong.
