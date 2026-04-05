Str = input("Nhập chuỗi nhị phân (chỉ gồm 0 và 1): ")
hop_le = True
for c in Str:
    if c not in "01":
        hop_le = False
        break
if hop_le:
    thap_phan = int(Str, 2)
    print(f"Số thập phân tương ứng: {thap_phan}")
else:
    print("Chuỗi nhập vào không phải là chuỗi nhị phân hợp lệ.")