import libs.xu_ly_thong_tin_nhanvien as xltt
print("____ Chức Năng ____")
print("1, Nhập thông tin")
print("2, Tính lương")
print("3, In ra danh sách nhân viên")
print("4, Sắp xếp rồi in ra màn hình")
print("5. Lưu dữ liệu")
print("0, Escape")
while(True):
   n = int(input("Nhập chức năng muốn thao tác: "))
   if(n == 1): xltt.nhap_thong_tin()
   if(n == 2): xltt.tinh_luong()
   if(n == 3): xltt.in_ra()
   if(n == 4): xltt.sap_xep_hien_thi()
   if(n == 5): xltt.luu_du_lieu()
   if(n == 0):
      print("Tmạm Bmiệt!")
      break