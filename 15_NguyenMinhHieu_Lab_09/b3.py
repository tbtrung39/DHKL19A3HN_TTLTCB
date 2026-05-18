def luy_thua(n, a):
   if(n == 0):
      return 1
   if(n == 1):
      return a
   return a * luy_thua(n-1, a)
n = int(input("Nhập n: "))
a = int(input("Nhập a: "))
print(luy_thua(n, a))