# BAI TAP 4.2 - TRUONG HOP GAY LOI KHI EP KIEU

# 1. Thu ep "abc" sang so nguyen
try:
    so_1 = int("abc")
    print("So 1:", so_1)
except ValueError as e:
    print("Loi khi int('abc'):", e)


# 2. Thu ep "3.14" truc tiep sang so nguyen
try:
    so_2 = int("3.14")
    print("So 2:", so_2)
except ValueError as e:
    print("Loi khi int('3.14'):", e)


# 3. Cach lam dung:
# Ep "3.14" sang float truoc, sau do ep sang int
so_hop_le = int(float("3.14"))

print("So hop le sau khi ep kieu:", so_hop_le)