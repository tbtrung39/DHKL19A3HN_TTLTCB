print("Chương trình nhập số (nhập số âm để dừng):")

while True:
    n = float(input("Nhập một số bất kỳ: "))
    
    if n < 0:
        print("Bạn đã nhập số âm. Kết thúc chương trình!")
        break  # Thoát khỏi vòng lặp ngay lập tức
    
    print(f"Số bạn vừa nhập là: {n}")