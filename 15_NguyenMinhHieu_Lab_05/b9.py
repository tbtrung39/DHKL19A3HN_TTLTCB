str = input("Nhập một chuỗi ký tự: ")
max_str = ""
check_str = ""
i = 0
while(i < len(str)):
    if(str[i] == str[i - 1]):
        check_str += str[i]
    else:
        if(len(max_str) < len(check_str)):
            max_str = check_str
        check_str = str[i]
    i += 1
if(len(max_str) < len(check_str)):
    max_str = check_str
print("Ký tự con sau khi lọc:", max_str)