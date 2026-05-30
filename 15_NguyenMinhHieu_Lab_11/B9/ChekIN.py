with open("B9/PASSENGER.IN", "w") as file:
   file.write(input("Nhập số lượng khách bay: ") + "\n")
   n = int(input("Nhập số lượng hành khách gửi các đồ xách tay: "))
   for i in range(1, n+1):
      file.write(input(f"Nhập các khối lượng của từng đồ xách tay của hành khách thứ {i}: ") + "\n")
   print("Thông tin đã được đưa lên hệ thống!")
weight_lst = []
with open("B9/PASSENGER.IN", "r") as file:
   read = file.readlines()
   i = 1
   while(i <= n):
      weight_lst.append(read[i].split())
      i += 1
w_lst = []
item_out = []
weight_out = []
for info in range(len(weight_lst)):
   if(len(weight_lst[info]) > 5):
      item_out.append(info)
for info in weight_lst:
   add = 0
   for w in info:
      add += float(w)
   w_lst.append(add)
for i in range(len(w_lst)):
   if(float(w_lst[i]) > 23):
      weight_out.append(i)
with open("B9/WEIGHT.OUT", "w") as f:
   for i in w_lst:
      f.write(str(i) + "\n")
set_out = set(item_out + weight_out)
with open("B9/CANCELED.OUT", "w", encoding="utf-8") as f:
   for i in sorted(set_out):
      if(i in weight_out and i not in item_out):
         f.write(f"{i + 1} -> Số thứ tự của khách có tổng trọng lượng đồ xách tay quá 23kg!" + "\n")
      elif(i not in weight_out and i in item_out):
         f.write(f"{i + 1} -> Số thứ tự của khách có tổng đồ xách tay vượt quá mức quy định!" + "\n")
      elif(i in weight_out and i in item_out):
         f.write(f"{i + 1} -> Số thứ tự của khách có tổng trọng lượng và số lượng đồ vượt quá mức quy định!" + "\n")