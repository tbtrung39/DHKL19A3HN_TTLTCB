ki_tu = input("Nhập một kí tự: ")

for i in range(32, 127):   
    if chr(i) == ki_tu:
        print("Giá trị ASCII của", ki_tu, "là:", i)
        break