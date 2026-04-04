str = "iads8gaioveiiabcia23vohfpiufsda" \
"uoags34diadiaf023iea" \
"23tf7wdtfsdgrule34aeoi"
while(True):
    check = input("Nhập một ký tự để kiểm tra: ")
    if(len(check) != 1):
        print("Chỉ nhập một ký tự!")
    else:
        count = 0
        for i in str:
            if(i == check):
                count += 1
        print(f"ký tự {check} xuất hiện {count} lần!")
    break