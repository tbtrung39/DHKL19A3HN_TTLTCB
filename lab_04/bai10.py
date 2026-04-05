n = input("Nhập số thập phân: ")

while n != "":
    ch = n[0]

    if ch == '0': print("không", end=" ")
    elif ch == '1': print("một", end=" ")
    elif ch == '2': print("hai", end=" ")
    elif ch == '3': print("ba", end=" ")
    elif ch == '4': print("bốn", end=" ")
    elif ch == '5': print("năm", end=" ")
    elif ch == '6': print("sáu", end=" ")
    elif ch == '7': print("bảy", end=" ")
    elif ch == '8': print("tám", end=" ")
    elif ch == '9': print("chín", end=" ")
    elif ch == '.': print("chấm", end=" ")

    n = n[1:] 
 