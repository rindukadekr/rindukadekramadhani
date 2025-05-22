# PPDB Sederhana

Aplikasi **PPDB Sederhana** adalah sistem informasi pendaftaran peserta didik baru berbasis web menggunakan Flask, SQLAlchemy, dan Bootstrap.

## Fitur Utama

- Registrasi dan login siswa
- Verifikasi data siswa oleh admin
- Status pendaftaran: Pending, Accepted, Rejected
- Upload foto ijazah
- Pembayaran sesuai jurusan
- Dashboard admin: verifikasi, terima/tolak, hapus data, lihat pembayaran
- Halaman informasi sekolah, visi & misi

## Cara Menjalankan

1. **Clone repository ini**  
   (atau copy seluruh folder ke komputer Anda)

2. **Buat virtual environment & install dependencies**

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**

   ```
   python run.py
   ```

4. **Akses di browser**  
   Buka [http://localhost:5000](http://localhost:5000)

## Akun Admin Default

- **Username:** admin
- **Password:** admin123

## Struktur Folder

```
ppdb sederhana/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   ├── templates/
│   └── static/
├── uploads/
├── run.py
├── requirements.txt
└── README.md
```

## Catatan

- Data akan tetap tersimpan selama file database (`app.db`) tidak dihapus.
- Untuk menambah/mengubah kolom database, gunakan Flask-Migrate.
- Folder `uploads/` digunakan untuk menyimpan file ijazah yang diupload siswa.

## Lisensi

Aplikasi ini bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.
