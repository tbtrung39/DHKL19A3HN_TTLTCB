import math

def tinh_tong_bai_2_while():
    n = int(input("Nhập số lượng phần tử n: "))
#a)
    S_a = 0
    i = 1
    while i <= n:
        if i % 2 != 0:
            S_a += 1 / i
        else:
            S_a -= 1 / i
        i += 1  
#b)           
    S_b = 0
    i = 1
    while i <= n:
        S_b += 1 / (i * (i + 1))
        i += 1
#c)       
    S_c = 0
    i = 2
    while i <= n + 1:
        S_c += 1 / math.sqrt(i)
        i += 1
        
    print(f"\nKết quả câu a (S_a): {S_a}")
    print(f"Kết quả câu b (S_b): {S_b}")
    print(f"Kết quả câu c (S_c): {S_c}")

tinh_tong_bai_2_while()