str = input("Nhập vào một chuỗi: ")
num = "" 

for c in str:
    if '0' <= c <= '9':
        num += c
if num == "":
    print("Không có số nào trong chuỗi")
else:
    n = int(num)
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    print("Chuỗi số: ", num)

    if sum == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")

  
