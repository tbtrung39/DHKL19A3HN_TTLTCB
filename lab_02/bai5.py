while True:
    thang = int(input("Nhập tháng (1-12): "))
    if 1 <= thang <= 12:
        cac_thang = ["January", "February", "March", "April", "May", "June", 
                     "July", "August", "September", "October", "November", "December"]
        print(f"Tên tháng: {cac_thang[thang-1]}")
        break
    else:
        print("Tháng không hợp lệ, nhập lại!")