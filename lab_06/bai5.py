import random
lst = []  
for i in range(1000):  
    so = random.randint(1, 99999)  
    lst.append(so) 
print(lst)
print("So luong phan tu:", len(lst))
print("5 phan tu dau:", lst[:5])