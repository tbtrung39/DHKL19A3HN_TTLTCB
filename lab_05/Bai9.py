Str = input("Nhập chuỗi: ")
max_sub = ""
current_sub = ""

for i in range(len(Str)):
    if i == 0:
        current_sub = Str[i]
    elif Str[i] == Str[i-1]:
        current_sub += Str[i]
    else:
        if len(current_sub) > len(max_sub):
            max_sub = current_sub
        current_sub = Str[i]

if len(current_sub) > len(max_sub):
    max_sub = current_sub
    
print("Chuỗi thỏa mãn:", max_sub)