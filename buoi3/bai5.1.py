import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print("Khoang cach giua", diem_a, "va", diem_b,
      "la:", round(khoang_cach, 2))

cac_diem = [(0, 0), (3, 4), (6, 8)]

goc = (0, 0)

x0, y0 = goc

for diem in cac_diem:
    x, y = diem

    khoang_cach = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)

    print("Diem", diem,
          "cach goc toa do la:",
          round(khoang_cach, 2))