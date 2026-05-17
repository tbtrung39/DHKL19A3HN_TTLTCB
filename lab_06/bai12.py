tong_tien = 0
print("Nhập nhật ký giao dịch :")
while True:
    s = input()
    if not s:
        break
    parts = s.split()
    action = parts[0]
    amount = int(parts[1])
    if action == "D":
        tong_tien += amount
    elif action == "W":
        tong_tien -= amount
print("Số dư cuối cùng:", tong_tien)