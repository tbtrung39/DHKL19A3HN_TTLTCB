import b7_module as md
A = md.sinh_day_a()
print(f"Dãy A ngẫu nhiên được sinh ra là: ")
print(A)
B = md.hien_snt_chia_het_7(A)
print("Các số nguyên tố chia hết cho 7 là: ")
print(B)
C = md.tong_so_le_trong_day(A)
print("Tổng các số lẻ thuộc dãy A là: ")
print(C)
D = md.kiem_tra_so_chinh_phuong(A)
print("Đang tìm số chính phương...")
if(D):
   print(D)
else:
   print("Không có số chính phương nào trong dãy!")