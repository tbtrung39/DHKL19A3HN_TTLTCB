def tinh_X(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 1
    
    ket_qua = 0
    for i in range(n):
        ket_qua += (n - i) ** 2 * tinh_X(i, memo)
    
    memo[n] = ket_qua
    return ket_qua

n = int(input("Nhập n: "))
X_n = tinh_X(n)

print(f"X_{n} = {X_n}")
