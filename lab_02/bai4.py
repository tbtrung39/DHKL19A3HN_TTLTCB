so = int(input("Nhap vao mot so nguyen: "))
if so>100 or so <=-100:
    a = abs(so)
    sohangtram = (a//100)/10 #chia nguyen cho 100,lay phan du /10
    print("chu so hang tram la: ", sohangtram)
else:
    print("chu so hang tram la 0")
