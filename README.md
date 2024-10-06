# PiComp - Image Compressor
![PiComp](https://github.com/user-attachments/assets/0e9176ac-4e60-4ef6-b755-6b1ab35494f6)

### [🌐 Live Demo](https://picomp.pythonanywhere.com/)
**PiComp** adalah aplikasi berbasis web sederhana yang memungkinkan pengguna untuk mengunggah dan mengompres gambar sesuai ukuran yang diinginkan. Dengan antarmuka yang mudah digunakan, kamu dapat mengompres gambar dengan cepat tanpa mengorbankan kualitas visual.

## Fitur Utama
- **Resize Opsional**: Memungkinkan pengguna untuk mengubah dimensi gambar secara otomatis selama proses kompresi.
- **Kompresi Gambar**: Kompres gambar hingga ukuran tertentu (contoh: 200 KB) tanpa kehilangan banyak kualitas.
- **Antarmuka Sederhana**: Antarmuka yang minimalis dan responsif membuat proses kompresi gambar lebih mudah.
- **Mendukung Banyak Format**: Mendukung berbagai format gambar populer seperti JPEG dan PNG.

## Teknologi yang Digunakan
- **HTML5 & CSS3**: Membentuk tampilan antarmuka pengguna.
- **JavaScript**: Menyediakan interaktivitas dasar pada halaman.
- **Django**: Framework Python untuk web.
- **Pillow**: Library Python untuk manipulasi gambar.

## Instalasi di Localhost
1. **Clone repositori ini ke direktori lokalmu menggunakan Git**:
    ```bash
    git clone https://github.com/RozhakXD/PiComp.git
    cd "PiComp"
    ```
2. **Untuk mengisolasi dependensi proyek, buatlah virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # di Linux/Mac
    venv\Scripts\activate  # di Windows
    ```

3. **Instal semua dependensi yang diperlukan dari `requirements.txt`**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Jalankan migrasi database Django**:
    ```bash
    python manage.py migrate
    ```

5. **Sekarang, kamu dapat menjalankan aplikasi di localhost:**
    ```bash
    python manage.py runserver
    ```

## Persyaratan Sistem
Pastikan sistemmu memenuhi persyaratan berikut sebelum menginstal **PiComp**:

- **Pillow library** untuk manipulasi gambar
- **Python 3.6+**
- **pip** (Python package installer)
- **Django 3.x+**

## Cara Menggunakan
1. **Unggah Gambar**: Klik pada bagian "Select Image" untuk memilih gambar yang akan diunggah.
2. **Pilih Ukuran**: Masukkan ukuran target gambar (contoh: 200 KB) pada kolom "Size".
3. **Resize Opsional**: Centang opsi "Resize Image?" jika ingin mengubah dimensi gambar.
4. **Kompres Gambar**: Klik tombol Compress Image untuk memulai proses kompresi.
5. **Download Hasil**: Gambar hasil kompresi akan tersedia untuk diunduh setelah proses selesai.

## Troubleshooting
- **Gambar tidak terkompresi sesuai ukuran yang diinginkan**
    - Pastikan format gambar yang diunggah didukung (JPEG atau PNG). Hasil kompresi dapat bervariasi tergantung pada format dan kualitas gambar awal.
- **Error**: `Pillow library not found`
    - Pastikan Pillow telah diinstal dengan menjalankan `pip install pillow`.

## Dukungan Proyek
Jika kamu merasa proyek ini bermanfaat, pertimbangkan untuk mendukung pengembangan lebih lanjut dengan berdonasi. Dukunganmu akan sangat berarti untuk menjaga proyek ini terus berjalan dan berkembang! ❤️

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

Terima kasih banyak atas dukunganmu!

## Tangkapan Layar
![Results](https://github.com/user-attachments/assets/3a8fb97e-8a04-4c24-a69d-e0db8b832111)

## Changelog
- **v1.0.0**: Rilis awal, fitur utama kompresi gambar dengan opsi resize.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [LICENSE](https://github.com/RozhakXD/Softwarcc/blob/main/LICENSE) untuk informasi lebih lanjut.

##
```python
print("Terima kasih telah menggunakan PiComp! 🌟")
```
##
