def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_list(arr, n):
    if n == 1:
        return arr[0]
    return gcd(arr[n - 1], gcd_list(arr, n - 1))


n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

print("UCLN =", gcd_list(a, n))