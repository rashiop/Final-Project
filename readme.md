## What
Supervised classification predicting covid 19
[dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)



## API
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

Workflow
<img width="372" alt="Screenshot 2022-12-02 at 23 01 36" src="https://user-images.githubusercontent.com/31156788/205334258-6d3328ca-5d74-4776-a996-79762dc4c8b3.png">


## Project
### Background
Selama pandemi, salah satu masalah utama bidang kesehatan adalah kekurangan medical resources dan mendistribusikannya karena banyaknya jumlah pasien. Sehingga untuk dapat memprediksi apakah seorang individual mungkin terdeteksi positif dengan tingkat keparahan tinggi bahkan sebelum mencari penanganan sangatlah penting untuk bisa memastikan resources diutamakan bagi yang benar-benar memerlukan.

Karena banyaknya jumlah pasien positif akan lebih baik jika cek bisa dilakukan dengan cepat atau malah oleh semua pihak (suster, keluarga pasien, pasien isolasi mandiri, dan lainnya) berdasarkan kondisi saat ini, status, dan medical history. Situs dengan API machine learning akan kita pilih karena bisa diakses kapan saja dari berbagai perangkat tanpa harus mengunduh terlebih dahulu.

### Project Architecture
??

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

## Kesimpulan dan refrensi
Model yang dipakai adalah KNN karena memiliki f1_score yang paling tinggi

### Future improvement
- deployment (terkendala masalah OTP kartu kredit)
- melakukan training ulang untuk mengurangi fitur yang double
- merapihkan label form untuk meningkatkan UX

### Referensi
- https://corona.kendalkab.go.id/berita/profil/kenalan-dengan-covid-19
- https://www.trivusi.web.id/2022/04/evaluasi-sistem-dengan-confusion-matrix.html
- https://www.kaggle.com/datasets/meirnizri/covid19-dataset
