'''11. Viết chương trình nhập vào giờ bắt đầu, giờ kết thúc và in ra số tiền khách thuê sân tập phải trả, 
biết rằng 5 giờ ≤ giờ bắt đầu ≤ giờ kết thúc ≤ 22 giờ.
'''

gio_bat_dau = float(input("Nhập số giờ bắt đầu: "))
gio_ket_thuc = float(input("Nhập số giờ kết thúc: "))

if 5 <=gio_bat_dau <= gio_ket_thuc <= 22:
    tien =  gio_ket_thuc - gio_bat_dau
    print("Số tiền phải trả là: ",tien)
else:
    print("Nhập sai giờ")      
