#a,
def s1(n):
   if(n == 1):
      return 1/2
   return (1/(n*(n+1))) + s1(n - 1)
n = int(input("Nhập n: "))
while(True):
   if(n <= 0):
      print("n phải lớn hơn 0!")
   else:
      break
print("S1 =", s1(n))
#b, 
def s2(m):
   if(m == 0):
      return 0
   if(m == 1):
      return 1
   return 1/(m*(s2(m-1)))
while(True):
   m = int(input("Nhập m: "))
   if(m <= 0):
      print("Hãy nhập số lớn hơn 0!")
   else:
      break
print("S2 =", s2(m) + s2(m-1))
#c,
def s3(x):
   if(x == 1):
      return 3**0.5
   if(x == 0):
      return 0
   return (3*n + s3(n-1))**0.5
while(True):
   x = int(input("Nhập x: "))
   if(x <= 0):
      print("Hãy nhập số lớn hơn 0!")
   else:
      break
print("S3=", s3(x))
#d,
def s4(y):
   if(y == 0):
      return 1
   return (y + 1)**(1/(y+1))
while(True):
   y = int(input("Nhập y: "))
   if(y <= 0):
      print("Hãy nhập số lớn hơn 0!")
   else:
      break
print("S4 =", s4(y))