n = int(input("Nhập số lượng thí sinh: "))
with open("B5/Sbd_Ten.txt", "w", encoding="utf-8") as f:
   for i in range(n):
      sbd = input(f"Nhập SBD của thí sinh thứ {i+1}: ")
      ho_ten = input(f"Nhập Họ tên của thí sinh thứ {i+1}: ")
      f.write(f"{sbd} {ho_ten}\n")

print("NHẬP SỐ PHÁCH")
with open("B5/Sbd_Ph.dat", "w", encoding="utf-8") as f:
   for i in range(n):
      sbd = input(f"Nhập SBD của thí sinh thứ {i+1}: ")
      phach = input(f"Nhập Số phách tương ứng với SBD {sbd}: ")
      f.write(f"{sbd} {phach}\n")

print("NHẬP ĐIỂM THI")
with open("B5/Phieu_Diem.txt", "w", encoding="utf-8") as f:
   for i in range(n):
      phach = input(f"Nhập Số phách thứ {i+1}: ")
      diem = input(f"Nhập Điểm số của số phách {phach}: ")
      f.write(f"{phach} {diem}\n")
ds_sbd_ten = []
with open("B5/Sbd_Ten.txt", "r", encoding="utf-8") as f:
   for line in f:
      du_lieu = line.split()
      if len(du_lieu) > 0:
         sbd = du_lieu[0]
         ho_ten = " ".join(du_lieu[1:])
         ds_sbd_ten.append([sbd, ho_ten])
ds_sbd_phach = []
with open("B5/Sbd_Ph.dat", "r", encoding="utf-8") as f:
   for line in f:
      du_lieu = line.split()
      if len(du_lieu) > 0:
         sbd = du_lieu[0]
         phach = du_lieu[1]
         ds_sbd_phach.append([sbd, phach])
ds_phach_diem = []
with open("B5/Phieu_Diem.txt", "r", encoding="utf-8") as f:
   for line in f:
      du_lieu = line.split()
      if len(du_lieu) > 0:
         phach = du_lieu[0]
         diem = float(du_lieu[1])
         ds_phach_diem.append([phach, diem])
danh_sach_thi_sinh = []
for item_diem in ds_phach_diem:
   phach = item_diem[0]
   diem = item_diem[1]
   sbd_tim_duoc = ""
   for item_phach in ds_sbd_phach:
      if item_phach[1] == phach:
         sbd_tim_duoc = item_phach[0]
         break
   ho_ten_tim_duoc = ""
   for item_ten in ds_sbd_ten:
      if item_ten[0] == sbd_tim_duoc:
         ho_ten_tim_duoc = item_ten[1]
         break
   if sbd_tim_duoc != "" and ho_ten_tim_duoc != "":
      danh_sach_thi_sinh.append([sbd_tim_duoc, ho_ten_tim_duoc, diem])

def lay_diem(item):
   return item[2]
danh_sach_thi_sinh.sort(key=lay_diem, reverse=True)
with open("B5/Ketqua.txt", "w", encoding="utf-8") as f_out:
   for ts in danh_sach_thi_sinh:
      sbd = ts[0]
      ho_ten = ts[1]
      diem = ts[2]
      f_out.write(f"{sbd} {ho_ten} {diem}\n")