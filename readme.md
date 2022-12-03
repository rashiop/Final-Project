## Project
Supervised classification predicting covid 19
[dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)

### Background
Selama pandemi, salah satu masalah utama bidang kesehatan adalah kekurangan medical resources dan mendistribusikannya karena banyaknya jumlah pasien. Sehingga untuk dapat memprediksi apakah seorang individual mungkin terdeteksi positif dengan tingkat keparahan tinggi bahkan sebelum mencari penanganan sangatlah penting untuk bisa memastikan resources diutamakan bagi yang benar-benar memerlukan.

Karena banyaknya jumlah pasien positif akan lebih baik jika cek bisa dilakukan dengan cepat atau malah oleh semua pihak (suster, keluarga pasien, pasien isolasi mandiri, dan lainnya) berdasarkan kondisi saat ini, status, dan medical history. Situs dengan API machine learning akan kita pilih karena bisa diakses kapan saja dari berbagai perangkat tanpa harus mengunduh terlebih dahulu.

### Workflow
1. Persiapan Data
<img width="111" alt="Screenshot 2022-12-03 at 14 41 24" src="https://user-images.githubusercontent.com/31156788/205430501-fd179373-e23f-4a0a-b20a-90952b9b346f.png">
2. EDA
<img width="99" alt="Screenshot 2022-12-03 at 14 45 57" src="https://user-images.githubusercontent.com/31156788/205430631-48ec9ae5-b540-48a5-86db-ac8a38759f70.png">
3. Preprocessing dan Feature Engineering
<img width="110" alt="Screenshot 2022-12-03 at 14 49 27" src="https://user-images.githubusercontent.com/31156788/205430744-236fdfdd-65dd-45f5-a607-30aceb338655.png">
4. Modeling
<img width="80" alt="Screenshot 2022-12-03 at 14 54 30" src="https://user-images.githubusercontent.com/31156788/205430914-15a6a293-1359-4397-810a-e8f0cb54c9f0.png">

### Project Architecture
<img width="449" alt="Screenshot 2022-12-03 at 15 10 54" src="https://user-images.githubusercontent.com/31156788/205431400-46a6ced0-489e-4a7f-942e-875cfdb501df.png">

Seharusnya
<img width="449" alt="Screenshot 2022-12-03 at 15 11 52" src="https://user-images.githubusercontent.com/31156788/205431430-0372b05c-64d2-4901-8264-c05c40ffbc6c.png">

### Output project
Machine learning solution yang disajikan dalam bentuk API dan form dengan metrics f1_score > 70%.

## Cara pemakaian
Membuka aplikasi dan mensubmit form.
Ada dua tipe hasil:
- Selamat
```
Predicted Covid Death: Selamat - 0
```
- Meninggal
```
Predicted Covid Death: Meninggal - 1
```

### API
Untuk melakukan prediksi, diperlukan data
- USMER: integer range 1 (yes) dan 2 (no)
- MEDICAL_UNIT: integer range 1 (yes) dan 2 (no)
- PATIENT_TYPE: integer range 1 (yes) dan 2 (no)
- INTUBED: integer range 1 (yes) dan 2 (no)
- PNEUMONIA: integer range 1 (yes) dan 2 (no)
- PREGNANT: integer range 1 (yes) dan 2 (no)
- DIABETES: integer range 1 (yes) dan 2 (no)
- COPD: integer range 1 (yes) dan 2 (no)
- ASTHMA: integer range 1 (yes) dan 2 (no)
- INMSUPR: integer range 1 (yes) dan 2 (no)
- HIPERTENSION: integer range 1 (yes) dan 2 (no)
- OTHER_DISEASE: integer range 1 (yes) dan 2 (no)
- CARDIOVASCULAR: integer range 1 (yes) dan 2 (no)
- OBESITY: integer range 1 (yes) dan 2 (no)
- RENAL_CHRONIC: integer range 1 (yes) dan 2 (no)
- TOBACCO: integer range 1 (yes) dan 2 (no)
- CLASIFFICATION_FINAL: integer range 1 (yes) dan 2 (no)
- ICU: integer range 1 (yes) dan 2 (no)
- AGE_BIN: integer range 1-8
    - 1: 0-24
    - 2: 25-34
    - 3: 35-44
    - 4: 45-54
    - 5: 55-64
    - 6: 65-74
    - 7: 75-84
    - 8: >= 85
 
Response dari API
Meninggal karena covid
```
{
  "res": 1,
  "error_msg": ""
}
```
Tidak meninggal
```
{
  "res": 0,
  "error_msg": ""
}
```



## Kesimpulan dan refrensi
Model yang dipakai adalah KNN karena memiliki f1_score yang paling tinggi

## Cara menjalankan di local
0. Memiliki docker di local
1. Masuk ke root directory project di terminal & `docker compose up`

### Future improvement
- Live di cloud, karena masalah simcard (tidak bisa login karena OTP) jadi di local saja.
- melakukan training ulang untuk mengurangi fitur yang double
- merapihkan label form untuk meningkatkan UX

### Referensi
- https://corona.kendalkab.go.id/berita/profil/kenalan-dengan-covid-19
- https://www.trivusi.web.id/2022/04/evaluasi-sistem-dengan-confusion-matrix.html
- https://www.kaggle.com/datasets/meirnizri/covid19-dataset
