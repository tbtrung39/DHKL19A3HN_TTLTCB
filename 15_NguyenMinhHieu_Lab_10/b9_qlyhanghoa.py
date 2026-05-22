ma_mh = []
thong_tin = []
def nhap_thong_tin():
   tt = []
   n = int(input("Nhập số lượng mặt hàng muốn thêm:"))
   for i in range(1, n+1):
      while(True):
         ma = input(f"Nhập mã mặt hàng thứ {i}: ")
         if(len(ma) != 4):
            print("Mã mặt hàng chỉ có 4 ký tự!")
         else:
            ma_mh.append(ma)
            break
      ten = input(f"Nhập tên mặt hàng thứ {i}: ")
      don_vi_tinh = input(f"Nhập đơn vị tính mặt hàng thứ {i}: ")
      don_gia = int(input(f"Nhập đơn giá mặt hàng thứ {i}: "))
      so_luong = int(input(f"Nhập số lượng mặt hàng thứ {i}: "))
      tt = {
         "Tên mặt hàng": ten,
         "Đơn vị tính": don_vi_tinh,
         "Đơn giá": don_gia,
         "Số lượng": so_luong
      }
      thong_tin.append(tt)
      print(f"Đã thêm thông tin của mặt hàng thứ {i}!")
def tinh_thanh_tien():
   global thong_tin
   count = 0
   for i in thong_tin:
      i["Thành tiền"] = i["Số lượng"]*i["Đơn giá"]
      count += 1
      print(f"Đã tính xong cho {count} mặt hàng!")
   return thong_tin
def tinh_thue():
   global thong_tin
   count = 0
   for i in thong_tin:
      i["Thuế"] = int(i["Thành tiền"])*(10/100)
      count += 1
      print(f"Đã tính xong thuế VAT cho {count} mặt hàng!")
   return thong_tin
def sap_xep_n_hien_thi():
   global ma_mh
   global thong_tin
   thong_tin = sorted(thong_tin, key=lambda i: i["Thuế"], reverse=True)
   print("Danh sách các mặt hàng")
   print("_"*100)
   danh_sach = dict(zip(ma_mh, thong_tin))
   for i in danh_sach.items():
      print(i)
   print("_"*100)