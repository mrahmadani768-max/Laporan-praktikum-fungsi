# # PROGRAM 12.1 PENGENALAN FUNGSI
# # --- MEMBUAT FUNGSI ---

# def hello_world():
#     print("hello world")
#     print("Kepada Fauzan Zein")
#     print("Dan Juga Kepada Faza Biri Biri")

# hello_world()

# # PROGRAM 12.2 FUNGSI DENGAN ARGUMEN 
# # --- FUNGSI DENGAN ARGUMEN ---

# def hello_world(nama):
#     print(f"Selamat data di Dunia, (nama)")

# hello_world("Tiara")

# def tambah(angka_1, angka_2):
#     hasil = angka_1 + angka_2
#     print(f"{angka_1} + {angka_2} = {hasil}")

# tambah(1, 10)

# def say_hi(list_peserta):
#     data_peserta = list_peserta.copy()
#     for peserta in data_peserta:
#         print(f"Selamat datang {peserta}")

# kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]

# say_hi(kumpulan_mahasiswa)

# # PROGRAM 12.3 FUNGSI DENGAN RETURN 
# # template fungsi kembalian
# # def nama_fungsi(argumen):
# #       badan fungsi
# #       return output

# # fungsi kuadrat

# def kuadrat(inpu_angka):
#     output_kuadrat = inpu_angka**2
#     return output_kuadrat

# y = kuadrat(5)
# print(y)

# print(kuadrat(5))

# z = 10 + kuadrat (7)
# print(z)

# def fungsi_tambah(angka_1, angka_2):
#     return angka_1 + angka_2

# a = fungsi_tambah(10, 8)
# print(a)

# def operasi_matematika(angka_1, angka_2):
#     tambah = angka_1 + angka_2
#     kurang = angka_1 - angka_2
#     kali = angka_1 * angka_2
#     bagi = angka_1 / angka_2

#     return tambah, kurang, kali, bagi

# k,l,m,n = operasi_matematika(9,5)

# print(f"Hasil tambah = {k}")
# print(f"Hasil kurang = {l}")
# print(f"Hasil kali = {m}")
# print(f"Hasil bagi = {n}")

# # PROGRAM 12.4 DEFAULT ARGUMEN FUNGSI
# # CONTOH 1
# def say_hello(nama = "Ojul"):
#     print("Hello {nama}")

# say_hello("Ucup")
# say_hello()

# # CONTOH 2 
# def sapa_dia(nama, pesan = "Apa kabar?"):
#     print(f"hai {nama}, {pesan}")

# sapa_dia("Nanda", "Selamat pagi")
# sapa_dia("Budi")

# # CONTOH 3 
# def hitung_pangkat(angka, pangkat):
#     hasil = angka**pangkat
#     return hasil

# print(hitung_pangkat(2,4))

# hasil = hitung_pangkat(pangkat=3, angka=5)
# print(hasil)

# # CONTOH 4
# def faktorial(input_1=1, input_2=2, input_3=3, input_4=4):
#     hasil = input_1 * input_2 * input_3 * input_4
#     return hasil

# print(faktorial())
# print(faktorial(input_3=10))

# --- TUGAS PRAKTIKUM ---


# Program Menghitung Luas dan Volume Bangun Ruang

# Fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil


# Fungsi volume balok
def volume_balok(panjang, lebar, tinggi):
    hasil = panjang * lebar * tinggi
    return hasil


# Fungsi luas lingkaran
def luas_lingkaran(jari_jari):
    hasil = 3.14 * jari_jari ** 2
    return hasil


# Fungsi volume bola
def volume_bola(jari_jari):
    hasil = (4/3) * 3.14 * jari_jari ** 3
    return hasil


# Input luas persegi panjang
print("=== LUAS PERSEGI PANJANG ===")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

hasil_luas = luas_persegi_panjang(panjang, lebar)
print("Luas persegi panjang =", hasil_luas)


# Input volume balok
print("\n=== VOLUME BALOK ===")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

hasil_volume = volume_balok(panjang, lebar, tinggi)
print("Volume balok =", hasil_volume)


# Input luas lingkaran
print("\n=== LUAS LINGKARAN ===")
jari_jari = float(input("Masukkan jari-jari: "))

hasil_luas = luas_lingkaran(jari_jari)
print("Luas lingkaran =", hasil_luas)


# Input volume bola
print("\n=== VOLUME BOLA ===")
jari_jari = float(input("Masukkan jari-jari: "))

hasil_volume = volume_bola(jari_jari)
print("Volume bola =", hasil_volume)
