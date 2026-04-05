chuoi_nhi_phan = input("Nhap chuoi nhi phan (chi gom 0 va 1): ")
so_thap_phan = 0
so_mu = 0 
for i in range(len(chuoi_nhi_phan) - 1, -1, -1):
    if chuoi_nhi_phan[i] == '1':
        so_thap_phan = so_thap_phan + (2 ** so_mu)
    so_mu = so_mu + 1
print("So thap phan tuong ung la:", so_thap_phan)