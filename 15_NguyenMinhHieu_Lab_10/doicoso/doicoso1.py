def nhap_so_nguyen():
   while(True):
      n = int(input("Nhập một số nguyên: "))
      if(n < 0):
         print("Hãy nhập một số nguyên dương!")
      else:
         print(n)
         break
   return n
def Dec_to_Bin(n):
   if(n == 0):
      print(n)
   Bin = ""
   while(n > 0):
      Bin = str(n % 2) + Bin
      n //= 2
   print(Bin)
   return Bin
def Dec_to_Oct(n):
   if(n == 0):
      print(n)
   Oct = ""
   while(n > 0):
      Oct = str(n % 8) + Oct
      n //= 8
   print(Oct)
   return Oct
def Dec_to_Hex(n):
   if(n == 0):
      print(n)
   hex_list = "0123456789ABCDEF"
   Hex = ""
   while(n > 0):
      i = n % 16
      Hex = hex_list[i] + Hex
      n //= 16
   print(Hex)
   return Hex