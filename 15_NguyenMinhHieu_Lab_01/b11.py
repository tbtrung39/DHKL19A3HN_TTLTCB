n = int(input("Nhập số lần tung xúc sắc: "))

triple_6 = (1/6)**3
print("Xác suất để 1 lần tung được cả 3 mặt 6 là P(triple_6): (1/6)**3", triple_6)
untriple_6 = 1-triple_6
print("Xác suất để không tung ra được cả 3 mặt 6 là P(untriple_6): 1 - P(triple_6)", untriple_6)
n_lan_untrip = untriple_6**n
print("Xác suất tung n lần mà không ra mặt 6 nào là p((untriple_6)n): P(untriple_6)**n", n_lan_untrip)
xs_it_nhat_1_lan_trip = 1 - n_lan_untrip
print(f"Xác xuất để khi tung {n} lần có ít nhất 1 lần ra 3 mặt 6 là:", xs_it_nhat_1_lan_trip)
