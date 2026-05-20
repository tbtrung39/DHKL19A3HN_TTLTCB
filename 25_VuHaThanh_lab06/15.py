danh_sach_sinh_vien = []

print("Nhập thông tin (Tên, Tuổi, Điểm). Nhập 'xong' để dừng.")

while True:
    thong_tin = input("Nhập (ví dụ: Tom,19,80): ")
    if thong_tin.lower() == 'xong':
        break
    phan_tu = thong_tin.split(',')
    
    if len(phan_tu) == 3:
        name = phan_tu[0].strip()
        age = int(phan_tu[1].strip())    
        score = int(phan_tu[2].strip()) 
        danh_sach_sinh_vien.append((name, age, score))
    else:
        print("Vui lòng nhập đúng định dạng: Tên, Tuổi, Điểm")
danh_sach_sinh_vien.sort()
print("\nDanh sách sau khi đã sắp xếp:")
print(danh_sach_sinh_vien)