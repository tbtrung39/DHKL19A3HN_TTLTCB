def loc_ky_tu(str):
   chuoi_moi = ""
   ktcg = "ABCDEF"
   for i in str:
      if(i.isdigit()):
         chuoi_moi += i
      elif(i.upper() in ktcg):
         chuoi_moi += i.upper()
   print("Chuỗi sau khi lọc là:", chuoi_moi)
   return chuoi_moi
def check_co_so(str):
   co_so_hex = False
   co_so_dec = False
   co_so_oct = False
   for j in str:
      if j in "ABCDEF":
         co_so_hex = True
      elif j.isdigit():
         val = int(j)
         if val >= 8:
            co_so_dec = True
         elif val >= 2:
            co_so_oct = True
   if(co_so_hex):
      print(f"{str} là cơ số 16")
   elif(co_so_dec):
      print(f"{str} là cơ số 10")
   elif(co_so_oct):
      print(f"{str} là cơ số 8")
   else:
      print(f"{str} là cơ số 2")
def Bin_to_Dec(tl):
   Dec = 0
   for i in range(len(tl)):
      if(tl[i] == "1"):
         Dec += 2**(len(tl) - int(i + 1))
   return Dec
def Oct_to_Dec(tl):
   Dec = 0
   for i in range(len(tl)):
      Dec += int(tl[i])*(8**(len(tl) - int(i + 1)))
   return Dec
def doi_so(i):
   if(i == "A"): return "10"
   elif(i == "B"): return "11"
   elif(i == "C"): return "12"
   elif(i == "D"): return "13"
   elif(i == "E"): return "14"
   elif(i == "F"): return "15"
   else: return i
def Hex_to_Dec(tl):
   Dec = 0
   check_str = ""
   for i in tl:
      if(i.isdigit()):
         check_str += i
      else:
         check_str += i.upper()
   for i in range(len(check_str)):
      Dec += int(doi_so(check_str[i]))*(16**(len(check_str) - int(i + 1)))
   return Dec