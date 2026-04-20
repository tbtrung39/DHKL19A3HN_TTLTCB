n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(1, n + 1):
    if(n % i == 0):
        A.add(i)
    else:
        B.add(i)
print(f"Set chứa các số là ước của n là: {A}")
print(f"Set chứa các số không phải ước của n là: {B}")