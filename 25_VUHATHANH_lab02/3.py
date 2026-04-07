while True:
    thu = int(input("Nhập thứ (1-7): "))
    if 1 <= thu <= 7:
        break
    print("Thứ không hợp lệ, vui lòng nhập lại!")

ten_thu = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Kết quả: {ten_thu[thu-1]}")