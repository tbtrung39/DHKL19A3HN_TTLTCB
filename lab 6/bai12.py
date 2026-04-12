total_balance = 0
print("Nhập nhật ký giao dịch (Nhập dòng trống để kết thúc):")
while True:
    entry = input()
    if not entry:
        break
    parts = entry.split()
    type = parts[0]
    amount = int(parts[1])
    if type == "D":
        total_balance += amount
    elif type == "W":
        total_balance -= amount
print(f"Số tiền thực của tài khoản: {total_balance}")