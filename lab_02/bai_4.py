n = int((input("Nhap 1 so nguyen n: ")))
n = abs(n)  #giá trị tuyệt đối
if n < 100:
    print(0)
else:
    hang_tram = (n // 100) % 10
    print("chu so hang tram la: ", hang_tram)