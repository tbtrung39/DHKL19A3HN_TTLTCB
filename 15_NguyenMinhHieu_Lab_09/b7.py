def tim_bo_nghiem(i, n, tong_con_lai, nghiem_hien_tai, cac_bo_nghiem):
   if i == n - 1:
      if tong_con_lai >= 0:
         nghiem_hien_tai[i] = tong_con_lai
         cac_bo_nghiem.append(nghiem_hien_tai.copy())
      return
   for gt in range(0, tong_con_lai + 1):
      nghiem_hien_tai[i] = gt
      tim_bo_nghiem(i + 1, n, tong_con_lai - gt, nghiem_hien_tai, cac_bo_nghiem)
def ctc():
      n = int(input("Nhập số lượng biến n: "))
      N = int(input("Nhập tổng N: "))
      if n <= 0 or N < 0:
         print("Vui lòng nhập n > 0 và N >= 0!")
         return
      nghiem_hien_tai = [0] * n
      cac_bo_nghiem = []
      tim_bo_nghiem(0, n, N, nghiem_hien_tai, cac_bo_nghiem)
      print(f"\nTìm thấy {len(cac_bo_nghiem)} bộ nghiệm phù hợp:")
      for bo_nghiem in cac_bo_nghiem:
         bieu_thuc = " + ".join(map(str, bo_nghiem))
         print(f"{bieu_thuc} = {N}")
ctc()