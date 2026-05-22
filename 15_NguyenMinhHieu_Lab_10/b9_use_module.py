import b9_qlyhanghoa as qlhh
print("Chức năng (0 -> 4)")
print("0, Escape")
print("1, Nhập thông tin")
print("2, Tính thành tiền")
print("3, Tính thuế VAT")
print("4, Sắp xếp và hiển thị")
while(True):
   n = int(input("Nhập chức năng(0 -> 4): "))
   if(n == 0):
      print("Tạm biệt!")
      break
   elif(n == 1):
      qlhh.nhap_thong_tin()
   elif(n == 2):
      qlhh.tinh_thanh_tien()
   elif(n == 3):
      qlhh.tinh_thue()
   elif(n == 4):
      qlhh.sap_xep_n_hien_thi()
   else:
      print("Hãy nhập đúng chức năng!")