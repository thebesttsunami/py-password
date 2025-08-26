import random
import string

# Pilihan karakter: huruf kecil, huruf besar, angka
huruf = string.ascii_lowercase
huruf_besar = string.ascii_uppercase
angka = string.digits
semua = huruf + huruf_besar + angka

# Minta panjang password dari user
panjang = int(input("Masukkan panjang password: "))

# Pastikan password mengandung huruf kecil, huruf besar, dan angka
password = [
    random.choice(huruf),
    random.choice(huruf_besar),
    random.choice(angka),
]

# Tambahkan sisa karakter secara acak
password += random.choices(semua, k=panjang - len(password))

# Acak urutan password
random.shuffle(password)

# Gabungkan jadi string
password = ''.join(password)

print(f"Password rumit kamu: {password}")
