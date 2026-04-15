import random
danh_sach = []
for so in range(0, 201): 
    if so % 5 == 0 and so % 7 == 0: 
        danh_sach.append(so)  
print("Danh sach:", danh_sach)