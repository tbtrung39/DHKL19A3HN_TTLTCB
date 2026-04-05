n = input("Nhap mot so: ")
chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
ket_qua = []
for ky_tu in n:
    if ky_tu.isdigit():
        ket_qua.append(chu_so[int(ky_tu)])
print("Ket qua:", " ".join(ket_qua))