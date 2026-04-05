ky_tu = input("Nhập một ký tự: ")

bang_ascii = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69,
              'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}

if ky_tu in bang_ascii:
    print("Giá trị ASCII là:", bang_ascii[ky_tu])
else:
    print("Chưa có trong bảng!")