def tao_matrix_vuong():
   while(True):
      n = int(input("Nhập n: "))
      if(n <= 0):
         print("n phải lớn hơn hoặc bằng 0!")
      else:
         break
   matrix_A = []
   for i in range(1, n+1):
      sub_array = []
      for j in range(1, n+1):
         sub_array.append(int(input(f"Nhập phần tử thứ {j} cột {i}: ")))
      matrix_A.append(sub_array)
   return matrix_A
def in_dong_n_cot(A):
   print("Dòng của matrix A:")
   for row in A:
      print(row)
   print("Cột của matrix A:")
   column = []
   for r in A:
      for n in range(len(A)):
         for c in range(len(r)):
            column.append(A[c][n])
         print(column)
         column = []
      break
def matrix_chuyen_vi(A):
   print("Matrix chuyển vị của A là: ")
   AT = []
   column = []
   for r in A:
      for n in range(len(A)):
         for c in range(len(r)):
            column.append(A[c][n])
         print(column)
         AT.append(column)
         column = []
      break
   return AT
def kiem_tra_doi_xung(A):
   print("Kiểm tra đối xứng:")
   return matrix_chuyen_vi(A) == A