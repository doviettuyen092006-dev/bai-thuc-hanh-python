sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("Ho ten:", sinh_vien["ho_ten"])

print("Diem trung binh:", sinh_vien.get("diem_tb"))


print("Lop:", sinh_vien.get("lop", "Chua co"))