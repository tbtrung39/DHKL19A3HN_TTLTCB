while True:
    ky_tu = input("Nhap 1 ky tu: ")
    
    if len(ky_tu) == 1:
        break
    else:
        print("nhap lai")

print("Ma ASCII la:", ord(ky_tu))