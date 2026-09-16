# BAI TAP 4.1 - EP KIEU TUONG MINH

# 1. Chuyen chuoi sang so nguyen
chuoi_so = "25"
so = int(chuoi_so)

print("So nguyen:", so)
print("Kieu du lieu:", type(so))


# 2. Chuyen chuoi sang so thuc
so_thuc = float("3.14")

print("So thuc:", so_thuc)
print("Kieu du lieu:", type(so_thuc))


# 3. Chuyen Tuple sang List
danh_sach = list((1, 2, 3))

print("Tuple -> List:", danh_sach)


# 4. Chuyen List sang Tuple
bo_ba = tuple([4, 5, 6])

print("List -> Tuple:", bo_ba)


# 5. Chuyen List sang Set
# Set tu dong loai bo cac phan tu trung lap
tap_hop = set([1, 2, 2, 3, 3, 3])

print("List -> Set:", tap_hop)


# 6. Chuyen List cac Tuple sang Dictionary
tu_dien = dict([("a", 1), ("b", 2)])

print("List Tuple -> Dictionary:", tu_dien)