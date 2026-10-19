
# Praktik: Analisis Nilai Mahasiswa

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
lulus = nilai_lulus(nilai)
jumlah_data = len(nilai)

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai      : {nilai}")
print(f"Banyak data     : {jumlah_data}")
print(f"Total nilai     : {sum(nilai)}")
print(f"Rata-rata       : {rata_rata(nilai):.2f}")

if jumlah_data > 0:
    print(f"Nilai minimum   : {min(nilai)}")
    print(f"Nilai maksimum  : {max(nilai)}")
else:
    print("Nilai minimum   : Tidak tersedia")
    print("Nilai maksimum  : Tidak tersedia")

print(f"Nilai lulus     : {lulus}")
print(f"Jumlah lulus    : {len(lulus)}")
print(f"Belum lulus     : {jumlah_data - len(lulus)}")
