import csv
ds_nv = []
def nhap_thong_tin():
   n = int(input("Nhập số lượng nhân viên muốn thêm: "))
   for i in range(1, n + 1):
      ma_nv = input("Nhập mã nhân viên: ")
      ten_nv = input("Nhập tên nhân viên: ")
      while(True):
         chuc_vu = input("Nhập chức vụ: ").upper()
         if(chuc_vu not in ["TP", "PP", "NV"]):
            print("Chỉ có 3 chức vụ (TP; PP; NV)!")
         else:
            break
      while(True):
         he_so_luong = int(input("Nhập hệ số lương: "))
         if(str(he_so_luong).isalpha()):
            print("Hệ số lương chỉ có thể nhập dữ liệu dạng số!")
         elif(he_so_luong < 0):
            print("Hệ số lương phải lớn hơn hoặc bằng 0!")
         else:
            break
      print(f"Đã nhập xong cho nhân viên thứ {i}!")
      thong_tin = {
         "Mã nhân viên": ma_nv,
         "Tên nhân viên": ten_nv,
         "Chức vụ": chuc_vu,
         "Hệ số lương": he_so_luong
      }
      ds_nv.append(thong_tin)
def tinh_luong():
   if(not ds_nv):
      print("Danh sách đang trống!")
      return None
   count = 0
   for i in ds_nv:
      i["Lương"] = i["Hệ số lương"] * 1490000
      if(i["Chức vụ"] == "TP"):
         i["Phụ cấp chức vụ"] = 1000000
         i["Thực lĩnh"] = 1000000 + i["Lương"]
      elif(i["Chức vụ"] == "PP"):
         i["Phụ cấp chức vụ"] = 700000
         i["Thực lĩnh"] = 700000 + i["Lương"]
      elif(i["Chức vụ"] == "NV"):
         i["Phụ cấp chức vụ"] = 300000
         i["Thực lĩnh"] = 300000 + i["Lương"]
      count += 1
   print(f"Đã tính lương xong cho {count} nhân viên!")
def in_ra():
   print("_"*100)
   print("| Mã nhân viên | Tên nhân viên | Chức vụ | Hệ số lương | Lương | Phụ cấp chức vụ | Thực lĩnh |")
   for row in ds_nv:
      print("_"*200)
      print(row)
def sap_xep_hien_thi():
   danh_sach_nv = sorted(ds_nv, key = lambda tl: tl["Thực lĩnh"], reverse=True)
   print("_"*90)
   print("|Mã nhân viên| Tên nhân viên |Chức vụ|Hệ số lương| Phụ cấp chức vụ |   Thực lĩnh   |")
   for tl in danh_sach_nv:
      print("_"*90)
      print(f"|  {tl["Mã nhân viên"]}  | {tl["Tên nhân viên"]} |     {tl["Chức vụ"]}     |    {tl["Hệ số lương"]}    | {tl["Lương"]} |  {tl["Phụ cấp chức vụ"]}  |  {tl["Thực lĩnh"]}  |")
      print("_"*90)
def luu_du_lieu():
   if(not ds_nv):
      print("Danh sách đang trống!")
      return
   with open("B8/files/ds_nhanvien.csv", 'w', newline="", encoding="utf-8") as file:
      tde = ["Mã nhân viên", "Tên nhân viên", "Chức vụ", "Hệ số lương", "Lương", "Phụ cấp chức vụ", "Thực lĩnh"]
      w = csv.DictWriter(file, fieldnames=tde)
      w.writeheader()
      w.writerows(ds_nv)
   print("Đã lưu file!")
print("@.@")