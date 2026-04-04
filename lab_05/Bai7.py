Str = input("Nhập chuỗi: ")
so_str = ""
for c in Str:
    if c.isdigit():
        so_str += c

print("Chuỗi số còn lại:", so_str)

if so_str != "":
    so = int(so_str)
    is_prime = True
    if so < 2:
        is_prime = False
    else:
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                is_prime = False
                break
                
    if is_prime:
        print(so, "là số nguyên tố")
    else:
        print(so, "không phải là số nguyên tố")