import random as rd
lst = []
for i in range(1001):
    lst.append(rd.randint(1, 99999))
n_lst = sorted(lst, reverse=False)
print(n_lst)
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if(lst[j] > lst[j + 1]):
            val = lst[j]
            lst[j] = lst[j + 1]
            lst[j] = val
print(lst)