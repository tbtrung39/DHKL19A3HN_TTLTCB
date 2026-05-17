def tinh_S_a(n):
    if n == 1:
        return 1 / (1 * 2)
    else:
        return 1 / (n * (n + 1)) + tinh_S_a(n - 1)

def tinh_S_b(n):
    if n == 1:
        return 1
    else:
        giai_thua = 1
        for i in range(1, n + 1):
            giai_thua *= i
        return 1 / giai_thua + tinh_S_b(n - 1)

def tinh_S_c(n):
    if n == 1:
        return (3) ** 0.5
    else:
        return (3 * n + tinh_S_c(n - 1)) ** 0.5

def tinh_S_d(n):
    if n == 1:
        return 1 ** (1/3)
    else:
        return (n + tinh_S_d(n - 1) ** (1/3)) ** (1/3)

n = int(input("Nhập n: "))

S_a = tinh_S_a(n)
S_b = tinh_S_b(n)
S_c = tinh_S_c(n)
S_d = tinh_S_d(n)

print(f"S_a = {S_a:.6f}")
print(f"S_b = {S_b:.6f}")
print(f"S_c = {S_c:.6f}")
print(f"S_d = {S_d:.6f}")
