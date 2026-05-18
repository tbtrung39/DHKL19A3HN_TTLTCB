import random as rd
def thiet_lap_hoan_vi(A, result):
   if(not A):
      return result
   vt_nn = rd.randint(0, len(A)-1)
   phan_tu = A.pop(vt_nn)
   result.append(phan_tu)
   print("Dãy A sau khi pop:", A)
   return thiet_lap_hoan_vi(A, result)
def ctc():
   n = int(input("Nhập n: "))
   while(True):
      if(n <= 0):
         print("Hãy nhập số tự nhiên lớn hơn 0")
      else:
         break
   A = list(range(1, n + 1))
   print("Dãy A ban đầu:", A)
   result = []
   kq = thiet_lap_hoan_vi(A, result)
   print(kq)
   return
ctc()