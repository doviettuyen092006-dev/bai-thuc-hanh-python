ten_sv = ["An", "Binh", "Chi"]

# Them vao cuoi
ten_sv.append("Dung")

# Chen vao vi tri 1
ten_sv.insert(1, "Em")

print("Sau append va insert:", ten_sv)

# Xoa theo gia tri
ten_sv.remove("Chi")

# Xoa phan tu cuoi va lay gia tri vua xoa
pop_ra = ten_sv.pop()

print("Sau remove va pop:", ten_sv)
print("Phan tu da xoa:", pop_ra)

# Sap xep
ten_sv.sort()
print("Sau sort:", ten_sv)

# Dao nguoc
ten_sv.reverse()
print("Sau reverse:", ten_sv)

# Noi them List
ten_sv.extend(["Giang", "Hoa"])
print("Sau extend:", ten_sv)