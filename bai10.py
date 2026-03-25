n = int(input("Nhập số n: "))

if n <= 0:
    print("n không hợp lệ!")
else:
    i = 2
    print("Phân tích:", n, "=", end=" ")
    
    while n > 1:
        if n % i == 0:
            print(i, end="")
            n //= i
            if n > 1:
                print(" * ", end="")
        else:
            i += 1