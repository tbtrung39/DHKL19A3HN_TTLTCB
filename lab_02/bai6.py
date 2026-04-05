n = int(input("Nhap n:"))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n < 100 or n > 999:
    print("Nhap so có 3 chu so!")
else:
    a = n // 100
    b = (n // 10)%10
    c = n % 10
    print(chu_so[a],"trăm", end=' ')
    if b == 0 and c!= 0:
        print("linh", chu_so[c])
    elif b == 1:
        print("mươi", end=' ')
        if c == 5:
            print("năm")
        else:
            print(chu_so[c])
    elif b > 1:
        print(chu_so[b],"mươi",end=' ')
        if c == 1:
            print("mốt")
    elif c == 0:
        print(" ")
    else:
        print(chu_so[c])
