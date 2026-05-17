ds = int(input("Nhap danh sach: ").split())
assert all(x % 2 == 0 for x in ds),"co so khong phai so chan"
print("Tat ca deu la so chan")