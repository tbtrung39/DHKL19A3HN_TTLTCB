code = input("Nhập mã container (10 ký tự): ")

if len(code) != 10:
    print("Mã không hợp lệ!")
else:
    total = 0
    i = 0

    for ch in code:
        if ch == 'A' or ch == 'a': value = 10
        elif ch == 'B' or ch == 'b': value = 12
        elif ch == 'C' or ch == 'c': value = 13
        elif ch == 'D' or ch == 'd': value = 14
        elif ch == 'E' or ch == 'e': value = 15
        elif ch == 'F' or ch == 'f': value = 16
        elif ch == 'G' or ch == 'g': value = 17
        elif ch == 'H' or ch == 'h': value = 18
        elif ch == 'I' or ch == 'i': value = 19
        elif ch == 'J' or ch == 'j': value = 20
        elif ch == 'K' or ch == 'k': value = 21
        elif ch == 'L' or ch == 'l': value = 23
        elif ch == 'M' or ch == 'm': value = 24
        elif ch == 'N' or ch == 'n': value = 25
        elif ch == 'O' or ch == 'o': value = 26
        elif ch == 'P' or ch == 'p': value = 27
        elif ch == 'Q' or ch == 'q': value = 28
        elif ch == 'R' or ch == 'r': value = 29
        elif ch == 'S' or ch == 's': value = 30
        elif ch == 'T' or ch == 't': value = 31
        elif ch == 'U' or ch == 'u': value = 32
        elif ch == 'V' or ch == 'v': value = 34
        elif ch == 'W' or ch == 'w': value = 35
        elif ch == 'X' or ch == 'x': value = 36
        elif ch == 'Y' or ch == 'y': value = 37
        elif ch == 'Z' or ch == 'z': value = 38
        else:
            value = int(ch)

        w = value * (2 ** i)
        print(f"w{i} = {value} x 2^{i} = {w}")

        total += w
        i += 1

    print("Tổng =", total)

    check = total % 11
    print("Số kiểm tra =", check)