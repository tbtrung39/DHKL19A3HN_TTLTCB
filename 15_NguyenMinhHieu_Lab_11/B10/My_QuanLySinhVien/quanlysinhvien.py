import csv
ds_sv = []
def nhap_thong_tin():
   n = int(input("Nhập số thông tin muốn thêm: "))
   count = 0
   for i in range(1, n + 1):
      ma_sv = input("Nhập mã sinh viên: ")
      ho_ten = input("Nhập tên sinh viên: ")
      diem_tb = float(input("Nhập điểm trung bình: "))
      diem_rl = int(input("Nhập điểm rèn luyện: "))
      thong_tin = {
         "Mã sinh viên": ma_sv,
         "Họ và tên": ho_ten,
         "Điểm trung bình": diem_tb,
         "Điểm rèn luyện": diem_rl
      }
      ds_sv.append(thong_tin)
      count += 1
   print(f"Đã thêm thông tin của {count} học sinh!")
def tinh_diem():
   count = 0
   for i in ds_sv:
      i["Điểm tích luỹ"] = (i["Điểm trung bình"] + i["Điểm rèn luyện"])/2
      count += 1
   print(f"Đã tính điểm xong cho {count} sinh viên!")
def in_ds_luu_tt():
   if(not ds_sv):
      print("Danh sách trống!")
      return None
   for i in ds_sv:
      for j in i.items():
         print(j)
         print("_"*140)
   tde = ["Mã sinh viên", "Họ và tên", "Điểm trung bình", "Điểm rèn luyện", "Điểm tích luỹ"]
   with open("B10/files/ds_sinhvien.csv", 'w', encoding="utf-8") as file:
      write = csv.DictWriter(file, fieldnames=tde)
      write.writeheader()
      write.writerows(ds_sv)
   print("Đã lưu thông tin!")
def xap_sep():
   danh_sach_sv = sorted(ds_sv, key=lambda tl: tl["Điểm rèn luyện"], reverse=True)
   print("Đã sắp xếp xong!")
   return danh_sach_sv
def tim_tt():
   ds_sinh_vien = sorted(ds_sv, key=lambda tl: tl["Điểm tích luỹ"], reverse=True)
   print(ds_sinh_vien[0])