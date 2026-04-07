while True:
    thang = int(input("Nhập tháng (1-12): "))
    if 1 <= thang <= 12:
        break
    print("Tháng không hợp lệ, vui lòng nhập lại!")

ten_thang = ["January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"]
print(f"Kết quả: {ten_thang[thang-1]}")