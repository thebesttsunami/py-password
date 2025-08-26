import random

huruf = "abcdefghijklmnopqrstuvwxyz"
huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789"

semua = huruf + huruf_besar + angka

# minta panjang password
panjang = int(input("Masukkan panjang password: "))

# pastikan minimal ada 1 huruf kecil, 1 huruf besar, dan 1 angka
password = [
    random.choice(huruf),
    random.choice(huruf_besar),
    random.choice(angka)
]

# sisa karakter diisi random
sisa = panjang - 3
password += random.choices(semua, k=sisa)

# acak urutan biar tidak berurutan
random.shuffle(password)

# gabungkan jadi string
password = ''.join(password)

print(f"ini password kamu: {password}")
