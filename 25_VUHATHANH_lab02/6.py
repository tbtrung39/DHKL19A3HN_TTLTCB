n = int(input("Nhập số có 3 chữ số (100-999): "))
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10

chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

doc = chu_so[tram] + " trăm"

if chuc == 0:
    if don_vi != 0:
        doc += " lẻ " + chu_so[don_vi]
elif chuc == 1:
    doc += " mười " + (chu_so[don_vi] if don_vi != 5 else "lăm")
else:
    doc += " " + chu_so[chuc] + " mươi " + (chu_so[don_vi] if don_vi != 5 else "lăm")

print("Cách đọc:", doc.strip())

