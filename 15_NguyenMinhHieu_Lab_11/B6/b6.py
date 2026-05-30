with open('B6/text.txt', 'w', encoding='utf-8') as file:
   str = ("4 \n211  133  180  5\n192  168  1   254\n11   1   11   233")
   file.write(str)
with open('B6/text.txt', 'r') as f:
   read = f.readlines()
   print("Dòng 1 và 3:")
   print(read[0].strip())
   print(read[2].strip())
   print("Toàn bộ file:")
   for line in read:
      print(line.strip())
with open("B6/text.txt", "r") as f:
   read = f.readlines()
   cac_dong_so = read[1:]
   tat_ca_so = []
   for dong in cac_dong_so:
      cac_tu = dong.split()
      for tu in cac_tu:
         tat_ca_so.append(int(tu))
matrix_odd = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
index = 0
for line in range(4):
   for cột in range(4):
      if index < len(tat_ca_so):
         so_hien_tai = tat_ca_so[index]
         if so_hien_tai % 2 != 0:
            matrix_odd[line][cột] = so_hien_tai
         index += 1
with open("B6/ODD.txt", "w") as f_odd:
   for line in matrix_odd:
        for i in line:
            f_odd.write(f"{i}  ")
        f_odd.write("\n")
with open('B6/ODD.txt', 'r') as abc:
   odd = abc.readlines()
   print("Dòng cuối:")
   print(odd[3].strip())