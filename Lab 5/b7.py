Str = input("Nhập chuỗi: ")
num = ""
i = 0
while i < len(Str):
    if Str[i].isdigit():
        num += Str[i]
    i += 1
print("Chuỗi số:", num)
if num != "":
    n = int(num)
    s = 0
    i = 1
    while i < n:
        if n % i == 0:
            s += i
        i += 1
    if s == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải số hoàn hảo")