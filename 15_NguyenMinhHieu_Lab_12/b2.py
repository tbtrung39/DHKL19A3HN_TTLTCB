ds = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
try:
   chuoi = input("Nhập một chuỗi ký tự: ")
   chuoi = chuoi.lower()
   for i in chuoi:
      if(i not in ds):
         raise ValueError("Lỗi ký tự!!!")
   for i in range(len(chuoi) - 4):
      if(chuoi[i] == chuoi[i+1] and chuoi[i+1] == chuoi[i+2] and chuoi[i+2] == chuoi[i+3] and chuoi[i+3] == chuoi[i+4]):
         raise ValueError("Lỗi nhập trùng lặp!!!")
   for i in range(len(chuoi) - 3):
      if(chuoi[i] == chuoi[i+1] and chuoi[i+1] == chuoi[i+2] and chuoi[i+2] == chuoi[i+3]):
         raise ValueError("Lỗi nhập lặp lại!!!")
   for i in range(len(chuoi) - 1):
      if(chuoi[i] == chuoi[i+1]):
         raise ValueError("Lỗi nhập liệu!!!")
except Exception as e:
   print(e)