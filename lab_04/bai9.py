so_n = input("Nhập một số nguyên: ")
tong_cs = sum(int(d) for d in so_n if d.isdigit())
print(f"Tổng các chữ số là: {tong_cs}")