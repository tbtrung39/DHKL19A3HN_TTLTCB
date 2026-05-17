m = input("Nhập m: ")
n = input("Nhập n: ")

digits_m = set(m)
digits_n = set(n)

common_digits = digits_m.intersection(digits_n)

tong = 0
for digit in common_digits:
    tong = tong + int(digit)

print("Chữ số chung:", common_digits)
print("Tổng các chữ số chung:", tong)
