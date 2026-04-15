import random
lst = []
for i in range(1000):
    so = random.randint(1, 99999)
    lst.append(so)
print("5 phan tu dau ban dau:", lst[:5])
# Cach 1: Dung sorted()
lst_sorted = sorted(lst)
print("5 phan tu dau sau khi sap xep (sorted):", lst_sorted[:5])

# Cach 2: Khong dung sorted (bubble sort)
lst2 = lst.copy() 
n = len(lst2)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst2[j] > lst2[j + 1]:
            # doi cho 2 phan tu
            temp = lst2[j]
            lst2[j] = lst2[j + 1]
            lst2[j + 1] = temp
print("5 phan tu dau sau khi sap xep (thu cong):", lst2[:5])