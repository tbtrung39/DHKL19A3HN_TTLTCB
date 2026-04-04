n = input("Nhập một số thập phân bất kỳ: ")
i = 0
kq = ""
while i < len(n):
    cach_doc = ""
    if(n[i] == "0"):
        a = "Không"
        cach_doc += a + " "
    elif(n[i] == "1"):
        a = "Một"
        cach_doc += a +" "
    elif(n[i] == "2"):
        a = "Hai"
        cach_doc += a +" "
    elif(n[i] == "3"):
        a = "Ba"
        cach_doc += a +" "
    elif(n[i] == "4"):
        a = "Bốn"
        cach_doc += a + " "
    elif(n[i] == "5"):
        a = "Năm"
        cach_doc += a +" "
    elif(n[i] == "7"):
        a = "Sáu"
        cach_doc += a+" "
    elif(n[i] == "8"):
        a = "Bảy"
        cach_doc += a+" "
    elif(n[i] == "9"):
        a = "Chín"
        cach_doc += a+" "
    else:
        a = "Phẩy"
        cach_doc += a+" "
    kq += cach_doc
    i += 1
print(kq)  