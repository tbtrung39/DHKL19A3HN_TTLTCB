def is_perfect_number(n):
    if n < 2: return False
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i*i != n:
                total += n // i
    return total == n

s = input("Nhập chuỗi: ")
digit_str = "".join([c for c in s if c.isdigit()])
print(f"Chuỗi số còn lại: {digit_str}")

if digit_str:
    num = int(digit_str)
    if is_perfect_number(num):
        print(f"{num} là số hoàn hảo.")
    else:
        print(f"{num} không phải là số hoàn hảo.")
else:
    print("Không tìm thấy số trong chuỗi.")