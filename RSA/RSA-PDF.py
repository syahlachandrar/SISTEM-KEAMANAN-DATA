from PyPDF2 import PdfWriter, PdfReader

# buat objek pdf writer
out = PdfWriter()

# buka file pdf asli
file_path = "D:/.smt3/SKD/RSA/test.pdf"
file = PdfReader(file_path)

# identifikasi total halaman file
num = len(file.pages)

# program membaca setiap halaman file sesuai halaman yang diidentifikasi
for idx in range(num):
    # dapatkan halaman
    page = file.pages[idx]

    # tambahkan halaman ke objek PdfWriter
    out.add_page(page)

# masukkan password enkripsi (gunakan parameter user dan owner)
password = "pass"
out.encrypt(password, use_128bit=True)

# buat nama file output (file enkripsi)
output_path = "D:/.smt3/SKD/RSA/outputtest.pdf"

# buka file enkripsi untuk ditulis (mode "wb")
with open(output_path, "wb") as f:
    # simpan objek PdfWriter yang berisi halaman-halaman terenkripsi ke file
    out.write(f)

# tambahkan pesan sukses
print(f"File {file_path} berhasil dienkripsi dan disimpan di {output_path}")