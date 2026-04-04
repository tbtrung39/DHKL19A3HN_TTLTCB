ky_tu = input("Nhập 1 kí tự bất kì :")
if len(ky_tu)== 1:
    ma_ascii = ord(ky_tu)
    print("Giá trị ASCII của ký tự là :",ma_ascii)
else:
    if len(ky_tu) == 0 :
        print("Bạn chưa nhập ký tự nào ")
    else:
        print("Bạn chỉ được nhập 1 ký tự")