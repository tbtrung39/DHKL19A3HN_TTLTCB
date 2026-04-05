n = input("Nhap mot so: ")
chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
ket_qua = " "
for so in n:
    ket_qua += chu_so[int(so)] + " "
print("Ket qua:", ket_qua.strip())