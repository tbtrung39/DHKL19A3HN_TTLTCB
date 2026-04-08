n = int(input("Nhập số nguyên có 3 chữ số: "))
if 100 <= n <= 999:
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    doc_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    res = doc_so[tram] + " trăm"
    if chuc == 0 and don_vi != 0:
        res += " lẻ " + doc_so[don_vi]
    elif chuc != 0:
        res += " " + doc_so[chuc] + " mươi"
        if don_vi != 0: res += " " + doc_so[don_vi]
    print(res.capitalize())
else:
    print("Vui lòng nhập đúng số có 3 chữ số!")