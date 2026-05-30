with open("B7/m_num.txt", 'w') as file:
   m = int(input("Nhập số lượng số muốn thêm: "))
   for i in range(m):
      file.write(input(f"Nhập số thứ {i + 1}: ") + " ")
with open('B7/n_num.txt', 'w') as file:
   n = int(input("Nhập số lượng số muốn thêm: "))
   for j in range(n):
      file.write(input(f"Nhập số thứ {j + 1}: ") + " ")
with open('B7/m_num.txt', 'r') as f:
   f = f.readlines()
   ds_m = []
   for line in f:
      for i in line:
         if(i.isdigit()):
            ds_m.append(int(i))
set_m = set(ds_m)
with open('B7/n_num.txt', 'r') as ff:
   ff = ff.readlines()
   ds_n = []
   for line in ff:
      for j in line:
         if(j.isdigit()):
            ds_n.append(int(j))
set_n = set(ds_n)
set_chung = set_n.intersection(set_m)
print(set_chung)
print("Danh sách các số chung:")
with open('B7/so_chung.txt', 'w') as file:
   for i in set_chung:
      file.write(str(i) + ", ")
with open("B7/so_chung.txt", 'r') as file:
   file = file.read()
   print(file)