# VAN DUNG - TU DIEN ANH - VIET

# Tao tu dien Anh - Viet
tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

# Tra tu
print("Nghia cua hello:", tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))

print("Nghia cua computer:",
      tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

# Them tu moi
tu_dien_anh_viet["computer"] = "may tinh"

# Xoa mot tu
tu_dien_anh_viet.pop("table")

# In tu dien hien tai
print("\nTu dien hien tai:")

for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")