heights = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

so_sinh_vien = len(heights)
print("Số sinh viên:", so_sinh_vien)

tong = 0
for i in range(len(heights)):
    tong = tong + heights[i]
trung_binh = tong / so_sinh_vien
print("Chiều cao trung bình:", trung_binh)

unique_heights = set(heights)
print("Chiều cao khác nhau:", sorted(unique_heights))
