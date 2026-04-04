n = int(input("Nhập số nguyên dương cần phân tích: "))
print(f"Kết quả phân tích {n} thành thừa số nguyên tố là:", end=" ")
if n < 2:
    print(n)
else:
    i = 2
    temp = n
    flag_var = True
    while temp > 1:
        while temp % i == 0:
            if flag_var:
                print(i, end="")
                flag_var = False
            else:
                print(f" * {i}", end="")      
            temp //= i       
        i += 1
