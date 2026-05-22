import b8_Matranvuong as mtv
A = mtv.tao_matrix_vuong()
for row in A:
   print(*row)
row_n_col = mtv.in_dong_n_cot(A)
At = mtv.matrix_chuyen_vi(A)
flag_val = True
print("Kiểm tra matrix đối xứng!")
if(mtv.kiem_tra_doi_xung(A)):
   print(flag_val)
else:
   flag_val = False
   print(flag_val)