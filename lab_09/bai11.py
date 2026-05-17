def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua_kep(n - 2)

def tinh_tong_giai_thua_kep(k):
    tong = 0
    for i in range(1, k + 1):
        if i % 2 == 1:
            tong += giai_thua_kep(i)
        else:
            tong -= giai_thua_kep(i)
    return tong

k = int(input("Nhập k (k < 1000): "))

if k >= 1000:
    print("k phải nhỏ hơn 1000")
else:
    S = tinh_tong_giai_thua_kep(k)
    print(f"S = 1!!-2!!+3!!-4!!+...+(-1)^(k+1)k!! = {S}")
