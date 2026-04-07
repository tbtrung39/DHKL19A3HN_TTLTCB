n = int(input("Nhập n: "))
tong_nghich_dao = sum(1/i for i in range(1, n + 1))
print("Tổng nghịch đảo:", round(tong_nghich_dao, 4))
