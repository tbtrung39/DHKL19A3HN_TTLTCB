def tinh_Xn(n):
   if(n == 0):
      return 1
   tong = 0
   for i in range(n):
      hsX = (n - i)**2
      tong += hsX + tinh_Xn(i)
   return tong
n = int(input("Nhập n: "))
while(True):
   if(n <= 0):
      print("Hãy nhập số lớn hơn 0!")
   else:
      break
print(tinh_Xn(n))