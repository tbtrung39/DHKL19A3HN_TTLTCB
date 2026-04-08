while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0: break
    print("Nhập lại!")

s1 = sum(range(1, n + 1))
s2 = sum(2*i + 1 for i in range(n + 1)) # 1 + 3 + ... + (2n+1)
s3 = sum(2*i for i in range(1, n + 1))  # 2 + 4 + ... + 2n

print(f"S1 = {s1}, S2 = {s2}, S3 = {s3}")