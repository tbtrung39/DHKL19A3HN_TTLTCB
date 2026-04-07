n = 0
while n <= 0:
    n = int(input("Nhập n (n > 0): "))

s1 = sum(range(1, n + 1))
s2 = sum(i for i in range(1, 2*n + 2) if i % 2 != 0)
s3 = sum(i for i in range(2, 2*n + 1) if i % 2 == 0)

print(f"S1 = {s1}, S2 = {s2}, S3 = {s3}")

