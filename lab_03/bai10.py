n = int(input("Nhập số nguyên dương n: "))
print("Dạng phân tích thừa số nguyên tố của", n, "là:")
for i in range(2, n + 1):
    for j in range(n):
        if n % i == 0:
            print(i)
            n = n // i