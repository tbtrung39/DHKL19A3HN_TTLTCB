def quaylui(i, n, cau_hinh, used):
    if i == n:
        print(" ".join(map(str, cau_hinh)))
        return
    for v in range(1, n + 1):
        if not used[v]:
            cau_hinh[i] = v
            used[v] = True
            quaylui(i + 1, n, cau_hinh, used)
            used[v] = False
def in_hoan_vi_quay_lui():
      n = int(input("Nhập n: "))
      if n <= 0:
         print("Nhập số tự nhiên lớn hơn 0!")
         return
      print(f"các hoán vị của dãy [1, 2, ..., {n}]:")
      cau_hinh = [0] * n
      used = [False] * (n + 1)
      quaylui(0, n, cau_hinh, used)
in_hoan_vi_quay_lui()