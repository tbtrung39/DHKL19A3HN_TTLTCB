ki_tu = input("Nhap ki tu: ")
for i in range(32, 127):   
    if chr(i) == ki_tu:
        print("gia tr ASCII cua", ki_tu, "la:", i)
        break