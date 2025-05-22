# PPDB Sederhana

Aplikasi **PPDB Sederhana** adalah sistem informasi pendaftaran peserta didik baru berbasis web menggunakan Flask, SQLAlchemy, dan Bootstrap.

<!-- Galeri Foto Project (menggunakan link langsung ke gambar di repo GitHub) -->
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(6).png" alt="Halaman Utama PPDB Sederhana" width="600"/><br>
  <em>Halaman utama PPDB Sederhana dengan tombol akses utama.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(7).png" alt="Formulir Pendaftaran" width="400"/>
  <br><em>Formulir pendaftaran siswa baru yang mudah diisi.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(8).png" alt="Verifikasi Siswa" width="400"/>
  <br><em>Halaman verifikasi data siswa setelah registrasi.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(9).png" alt="Notifikasi Verifikasi Selesai" width="400"/>
  <br><em>Notifikasi bahwa data verifikasi telah dikirim dan menunggu persetujuan admin.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(10).png" alt="Dashboard Admin - Statistik" width="600"/>
  <br><em>Dashboard admin menampilkan statistik pendaftaran secara visual dan menarik.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(11).png" alt="Verifikasi Pendaftar oleh Admin" width="600"/>
  <br><em>Admin dapat memverifikasi, menerima, atau menolak pendaftar.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(12).png" alt="Peserta Diterima" width="600"/>
  <br><em>Daftar peserta yang telah diterima oleh admin.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(13).png" alt="Halaman Pembayaran" width="600"/>
  <br><em>Halaman pembayaran untuk siswa yang sudah diterima.</em>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/USERNAME/REPO/main/foto%20projek/Screenshot%20(14).png" alt="Pembayaran Berhasil" width="600"/>
  <br><em>Konfirmasi pembayaran berhasil dan data masuk ke dashboard admin.</em>
</p>

<!-- Ganti USERNAME dan REPO sesuai username dan nama repository GitHub Anda -->

## Fitur Utama

- Registrasi dan login siswa
- Verifikasi data siswa oleh admin
- Status pendaftaran: Pending, Accepted, Rejected
- Upload foto ijazah
- Pembayaran sesuai jurusan
- Dashboard admin: verifikasi, terima/tolak, hapus data, lihat pembayaran, statistik pendaftaran
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

3. **Inisialisasi database**

   ```
   flask db upgrade
   ```

4. **Jalankan aplikasi**

   ```
   python run.py
   ```

5. **Akses di browser**  
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
├── foto projek/
│   ├── Screenshot (6).png
│   ├── Screenshot (7).png
│   ├── Screenshot (8).png
│   ├── Screenshot (9).png
│   ├── Screenshot (10).png
│   ├── Screenshot (11).png
│   ├── Screenshot (12).png
│   ├── Screenshot (13).png
│   └── Screenshot (14).png
├── run.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── USER_MANUAL.md
```

## Catatan

- Data akan tetap tersimpan selama file database (`app.db`) tidak dihapus.
- Untuk menambah/mengubah kolom database, gunakan Flask-Migrate.
- Folder `uploads/` digunakan untuk menyimpan file ijazah yang diupload siswa.

## Lisensi

Aplikasi ini bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.

# rindukadekramadhani

f8ee35b18c7901793027724601ce056ccb133a9d
