from functools import reduce

def tinh_tong_so_chan():
    n = int(input("Nhap n: "))
    lst = list(range(1, n + 1))
    so_chan = list(filter(lambda x: x % 2 == 0, lst))

    if so_chan:
        tong = reduce(lambda x, y: x + y, so_chan)
        print(f"Tong cac so chan tu 1 den {n} la: {tong}")
    else:
        print("Khong co so chan nao.")

tinh_tong_so_chan()
