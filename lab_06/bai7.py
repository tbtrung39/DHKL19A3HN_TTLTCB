List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]

for x in List_:
    print(x)

print(List_[2][1])

import random
List_.append(["new", random.randint(1,100)])

tong = sum(x[1] for x in List_ if x[0] in ["tue","wed","sat","sun"])
print("Tong:", tong)