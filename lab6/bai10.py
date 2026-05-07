import random
ket_qua = [i for i in range(0, 201) if i % 5 == 0 and i % 7 == 0]
if len(ket_qua) > 0:
    so_ngau_nhien = random.choice(ket_qua)
    print(so_ngau_nhien)