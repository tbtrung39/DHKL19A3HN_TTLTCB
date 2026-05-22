import random as rd
def sinh_day_a():
   A = []
   for i in range(rd.randint(1, 100)):
      A.append(rd.randint(1, 1000))
   return A
def snt(i):
   if(i < 2):
      return False
   for j in range(2, int(i**0.5)):
      if(i % j == 0):
         return False
   return True
def hien_snt_chia_het_7(x):
   lst = []
   for i in x:
      if(snt(i) and i % 7 == 0):
         lst.append(i)
   return lst
def tong_so_le_trong_day(x):
   tong = 0
   for i in x:
      if(i % 2 != 0):
         tong += i
   return tong
def kiem_tra_so_chinh_phuong(x):
   lst_2 = []
   for i in x:
      if(i == int(i**0.5)):
         lst_2.append(i)
   if(lst_2 is None):
      return False
   else:
      return lst_2