tu_dien = {}
for i in range(1, 101):
    nhi_phan = bin(i).replace("0b", "")
    tu_dien[i] = nhi_phan

print(tu_dien)