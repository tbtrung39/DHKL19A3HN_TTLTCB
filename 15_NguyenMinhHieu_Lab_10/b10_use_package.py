import hinhhoc.my_triangle as htg, hinhhoc.my_square as hv
x = float(input("Nhập cạnh 1 của tam giác: "))
y = float(input("Nhập cạnh 2 của tam giác: "))
z = float(input("Nhập cạnh 3 của tam giác: "))
print("Đang kiểm tra tam giác...")
if(htg.is_triangle(x, y, z)):
   print("=> Là tam giác!")
   print(f"Chu vi hình tam giác: {htg.chuvi_tamgiac(x, y, z)}")
   print(f"Diện tích tam giác: {htg.S_tamgiac(x, y, z)}")
else:
   print("Không phải tam giác!")
print("_"*100)
while(True):
   a = float(input("Nhập chiều dài cạnh hình vuông: "))
   if(a < 0):
      print("Chiều dài cạnh phải lớn hơn 0!")
   else:
      print(f"Chu vi hình vuông: {hv.chuvi_hinhvuong(a)}")
      print("Diện tích hình vuông là:", hv.S_hinhvuong(a))
      break