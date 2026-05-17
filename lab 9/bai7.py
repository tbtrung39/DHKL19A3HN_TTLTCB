def solve(N, n, current=[]):
    if n == 1:
        print(current + [N])
        return
    for i in range(N + 1):
        solve(N - i, n - 1, current + [i])
N = int(input("Nhập N: "))
n = int(input("Nhập số biến n: "))
solve(N, n)