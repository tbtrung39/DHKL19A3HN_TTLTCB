while True:
    chuoi = input("Nhập số (chỉ gồm 1-4): ")
    
    for ky_tu in chuoi:
        if ky_tu == '0':
            print("không", end=" ")
        elif ky_tu == '1':
            print("một", end=" ")
        elif ky_tu == '2':
            print("hai", end=" ")
        elif ky_tu == '3':
            print("ba", end=" ")
        elif ky_tu == '4':
            print("bốn", end=" ")
        else:
            print("Sai zồi, nhập lại đi bbi!")
    
    break