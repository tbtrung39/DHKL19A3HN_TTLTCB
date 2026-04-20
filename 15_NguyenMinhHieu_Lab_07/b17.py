n = int(input("Nhập số sinh viên: "))
ttsv = []
for i in range(n):
    msv = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm sinh viên: "))
    thong_tin_sv = {
        "Mã sinh viên": msv,
        "Tên sinh viên": ten,
        "Điểm số": diem
    }
    ttsv.append(thong_tin_sv)
for j in ttsv:
    print(j)