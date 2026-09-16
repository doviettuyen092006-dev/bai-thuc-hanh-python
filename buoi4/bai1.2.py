sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

# Them khoa moi
sinh_vien["lop"] = "CNTT01"

# Sua diem trung binh
sinh_vien["diem_tb"] = 9.0

print("Sau khi them va sua:", sinh_vien)

# Xoa diem_tb va luu gia tri vua xoa
diem_cu = sinh_vien.pop("diem_tb")

print("Sau khi xoa:", sinh_vien)
print("Diem da xoa:", diem_cu)

# Cap nhat va them nhieu khoa
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

print("Sau khi update:", sinh_vien)