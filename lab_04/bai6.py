while True:
    chuoi = input("Nhap so tu 1 den 4: ")
    
    for ky_tu in chuoi:
        if ky_tu == '0':
            print("khong", end=" ")
        elif ky_tu == '1':
            print("mot", end=" ")
        elif ky_tu == '2':
            print("hai", end=" ")
        elif ky_tu == '3':
            print("ba", end=" ")
        elif ky_tu == '4':
            print("bon", end=" ")
        else:
            print("sai roi nhe bbi")
    break