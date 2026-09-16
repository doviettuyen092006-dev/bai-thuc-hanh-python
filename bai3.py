# BAI TAP 3.1 - DICTIONARY COMPREHENSION

diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

# Cong them 0.5 diem cho moi mon
diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print("Diem sau khi cong 0.5:", diem_cong_diem)

# Viet hoa ten mon hoc
ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print("Ten mon viet hoa:", ten_mon_viet_hoa)


# BAI TAP 3.2 - SO SANH NHANH VOI SET

mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

# Giao: mon hoc chung cua 2 hoc ky
print("Mon hoc chung:", mon_hoc_ky1 & mon_hoc_ky2)

# Hop: tat ca mon hoc cua 2 hoc ky
print("Tat ca mon hoc:", mon_hoc_ky1 | mon_hoc_ky2)

# Hieu: mon chi co o hoc ky 1
print("Mon chi co o hoc ky 1:", mon_hoc_ky1 - mon_hoc_ky2)