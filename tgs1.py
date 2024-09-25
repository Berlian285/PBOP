# 2D Segitiga
alas = int(input("Masukkan panjang alas segitiga: "))
tinggi = int(input("Masukkan tinggi segitiga: "))
luas = 0.5 * alas * tinggi
print("Luas Segitiga:", luas)

# 3D Kerucut
phi = 3.14
r  = int(input("Masukkan jari-jari kerucut: "))
t = int(input("Masukkan tinggi kerucut: "))
volume = (1/3) * phi * (r ** 2) * t
LuasPermukaan = phi * r * (r + (t ** 2 + r ** 2) ** 0.5)
print("Volume Kerucut:", volume)
print("Luas Permukaan Kerucut:", LuasPermukaan)
