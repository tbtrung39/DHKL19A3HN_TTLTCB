n = int(input("nhap: "))

print(f"phan tích thua so nguyen to cua ",n, "là: ", end="")

for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n //= i