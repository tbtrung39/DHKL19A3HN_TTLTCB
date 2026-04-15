danh_sach = []
n = int(input("Nhap so phan tu: "))
for i in range(n):
    ten = input("Nhap ten: ")
    tuoi = int(input("Nhap tuoi: "))
    diem = int(input("Nhap diem: "))
    
    bo = (ten, tuoi, diem) 
    danh_sach.append(bo)
danh_sach_sap_xep = sorted(danh_sach)
print("Danh sach sau khi sap xep:")
for phan_tu in danh_sach_sap_xep:
    print(phan_tu)