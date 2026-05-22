def is_triangle(a, b, c):
   if(a < 0 or b < 0 or c < 0):
      return False
   elif(a + b > c or a + c > b or b + c > a):
      return True
   else:
      return False
def chuvi_tamgiac(a, b, c):
   if(is_triangle(a, b, c)):
      return a + b + c
   else:
      print("Đây không phải hình tam giác!")
def S_tamgiac(a, b, c):
   p = (a + b + c)/2
   return (p*(p - a)*(p - b)*(p - c))**0.5