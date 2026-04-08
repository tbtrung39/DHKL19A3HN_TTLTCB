n = input("Nhập vào một số: ")

ket_qua = ""

for ky_tu in n:
    chu = ""
    if ky_tu == '0': chu = "không"
    elif ky_tu == '1': chu = "một"
    elif ky_tu == '2': chu = "hai"
    elif ky_tu == '3': chu = "ba"
    elif ky_tu == '4': chu = "bốn"
    elif ky_tu == '5': chu = "năm"
    elif ky_tu == '6': chu = "sáu"
    elif ky_tu == '7': chu = "bảy"
    elif ky_tu == '8': chu = "tám"
    elif ky_tu == '9': chu = "chín"

    if chu != "":
        ket_qua += chu + " "
print(f"Kết quả đọc là: {ket_qua.strip()}")