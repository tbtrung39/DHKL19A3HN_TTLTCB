import My_QuanLySinhVien.quanlysinhvien as qlsv
print("____ Chức Năng ____")
print("1, Nhập thông tin")
print("2, Tính điểm tích luỹ")
print("3, In ra danh sách nhân viên và lưu dữ liệu")
print("4, Sắp xếp")
print("5. In ra màn hình sinh viên có điểm tích luỹ cao nhất")
print("0, Escape")
while(True):
   n = int(input("Nhập chức năng muốn thao tác: "))
   if(n == 1): qlsv.nhap_thong_tin()
   if(n == 2): qlsv.tinh_diem()
   if(n == 3): qlsv.in_ds_luu_tt()
   if(n == 4): qlsv.xap_sep()
   if(n == 5): qlsv.tim_tt()
   if(n == 0):
      print("Tmạm Bmiệt!")
      break