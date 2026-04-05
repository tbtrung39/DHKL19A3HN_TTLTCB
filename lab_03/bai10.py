n = int(input("Nhập n: "))

print("Phân tích:", end=" ")

for i in range(2, n + 1):
    for j in range(n):   
        if n % i == 0:
            print(i, end=" ")
            n //= i