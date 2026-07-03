# CMS Company Profile

CMS Company Profile adalah aplikasi website profil perusahaan yang dibangun menggunakan [Wagtail](https://wagtail.org/) (CMS berbasis Django). Project ini memungkinkan admin mengelola konten perusahaan — mulai dari halaman utama, layanan, blog, hingga FAQ — melalui panel admin Wagtail tanpa perlu menyentuh kode.

## Fitur

- **Home Page** — halaman utama dengan showcase item (galeri unggulan) dan daftar paket layanan (service package) yang dapat diatur urutannya melalui admin.
- **Services** — halaman landing layanan dengan hero section, deskripsi pengantar, dan detail tiap layanan yang ditawarkan.
- **Blog** — halaman index dan detail artikel blog dengan tanggal publikasi, ringkasan (intro), dan konten rich text.
- **Navigation** — menu navigasi dinamis berbasis snippet (`MenuItem`) yang mendukung sub-menu (parent/child) dan urutan tampil kustom.
- **FAQ (Question & Answer)** — daftar pertanyaan & jawaban dengan status moderasi (pending/approved/rejected), opsi featured, dan kontrol tampil di halaman utama.
- **Search** — pencarian konten menggunakan `wagtail.search`.
- **Testimonials** — media pendukung untuk menampilkan testimoni pelanggan.

## Tech Stack

- **Backend**: Django 6.x, Wagtail 7.x
- **Database**: SQLite (default, `db.sqlite3`)
- **Frontend build**: Node.js, Tailwind CSS
- **Deployment**: Dockerfile tersedia di `mysite/`

## Struktur Project

```
mysite/
├── blog/                 # App blog (index & detail page)
├── home/                 # App halaman utama (showcase & service package)
├── services/             # App halaman layanan
├── navigation/            # App menu navigasi (snippet MenuItem)
├── question_and_answer/  # App FAQ
├── search/               # App pencarian
└── mysite/                # Settings & konfigurasi project Django
```

## Instalasi & Menjalankan Project

1. Buat virtual environment dan install dependency:
   ```bash
   cd mysite
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Jalankan migrasi database:
   ```bash
   python manage.py migrate
   ```
3. Buat superuser untuk mengakses admin Wagtail:
   ```bash
   python manage.py createsuperuser
   ```
4. Jalankan development server:
   ```bash
   python manage.py runserver
   ```
5. Akses situs di `http://127.0.0.1:8000/` dan admin panel di `http://127.0.0.1:8000/admin/`.

## Catatan

Project ini menggunakan source code Wagtail sebagai basis (folder `wagtail/`) dan aplikasi company profile (`mysite/`) dikembangkan di atasnya untuk keperluan pembelajaran CMS berbasis Wagtail.
