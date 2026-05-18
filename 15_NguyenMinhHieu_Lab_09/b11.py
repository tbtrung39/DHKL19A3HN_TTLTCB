def giai_thua_kep(n):
   if(n == 0 or n == 1):
      return 1
   return n * giai_thua_kep(n - 2)
while(True):
   n = int(input("Nhập n: "))
   if(n <= 0):
      print("Hãy nhập số lớn hơn 0!")
   else:
      break
print(f"Giai thừa kép của {n} là: {giai_thua_kep(n)}")
def tinh_gia_tri_giai_thua_kep():
   while(True):
      k = int(input("Nhập giá trị k: "))
      if(k >= 1000 and k <= 0):
         print("chỉ nhận giá trị k lớn hơn 0 và nhỏ hơn 1000!")
      else:
         break
   S = 0
   for i in range(1, k + 1):
      if(i % 2 != 0):
         S += giai_thua_kep(i)
      else:
         S -= giai_thua_kep(i)
   return S
print(tinh_gia_tri_giai_thua_kep())