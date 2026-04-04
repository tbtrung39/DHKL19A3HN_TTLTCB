while True:
    kt = input("Nhập vào một ký tự bất kỳ: ")
    if(len(kt) == 1):
        kt = ord(kt)
        print(kt)
        break
    elif(len(kt) == 0):
        print("Bạn chưa nhập gì cả!")
    else:
        print("Chỉ được nhập một ký tự!")