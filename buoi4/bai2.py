# HOAT DONG 2: DUYET DICTIONARY BANG FOR

diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

# 1. Duyet cac khoa bang keys()
print("=== TEN CAC MON HOC ===")
for mon in diem_mon_hoc.keys():
    print(mon)

# 2. Duyet cac gia tri bang values()
print("\n=== DIEM CAC MON HOC ===")
for diem in diem_mon_hoc.values():
    print(diem)

# 3. Duyet ca khoa va gia tri bang items()
print("\n=== MON HOC VA DIEM ===")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# 4. Tinh diem trung binh
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

diem_trung_binh = tong_diem / len(diem_mon_hoc)

print("\n=== KET QUA ===")
print("Tong diem:", tong_diem)
print("Diem trung binh:", round(diem_trung_binh, 2))