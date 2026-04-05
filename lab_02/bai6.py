n = int(input("nhap so nguyen n co 3 chu so: "))
if n < 100 or n > 999:
    print("nhap sai")
else:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    doc = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
    print(doc[a],"tram", end=' ')
    if b == 0 and c!= 0:
        print("linh", doc[c])
    elif b == 1:
        print("muoi", end=' ')
        if c == 5:
            print("lam")
        else:
            print(doc[c])
    elif b > 1:
        print(doc[b],"muoi",end=' ')
        if c == 1:
            print("mốt")
        elif c == 0:
            print(" ")
        else:
            print(doc[c])