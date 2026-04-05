while True:
    chuoi = input("Nhap so: ")

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
        elif ky_tu == '5':
            print("nam", end=" ")
        elif ky_tu == '6':
            print("sau", end=" ")
        elif ky_tu == '7':
            print("bay", end=" ")
        elif ky_tu == '8':
            print("tam", end=" ")
        elif ky_tu == '9':
            print("chin", end=" ")
        else:
            print("phay", end=" ")  
    print()    