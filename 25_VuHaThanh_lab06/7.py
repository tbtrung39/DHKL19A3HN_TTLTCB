import random
#1
List_ = [
    ["mon", 73], 
    ["tue", 89], 
    ["wed", 95], 
    ["thu", 103], 
    ["fri", 115], 
    ["sat", 128],
    ["sun", 120]
]

print("--- Yêu cầu 1: In danh sách List_ ---")
print(List_)
print("-" * 40)

#2
print("--- Yêu cầu 2: Lấy phần tử ---")
sublist_thu_3 = List_[2] 
phan_tu_thu_2 = sublist_thu_3[1]

print(f"Sublist ở vị trí thứ 3 là: {sublist_thu_3}")
print(f"Phần tử thứ hai trong sublist đó là: {phan_tu_thu_2}")
print("-" * 40)

#3
print("--- Yêu cầu 3: Kiểm tra độ dài và thêm sublist ngẫu nhiên ---")
print(f"Độ dài của danh sách hiện tại: {len(List_)} phần tử.")

cac_ngay = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
ngay_ngau_nhien = random.choice(cac_ngay)
so_ngau_nhien = random.randint(1, 200)
sublist_ngau_nhien = [ngay_ngau_nhien, so_ngau_nhien]
List_.append(sublist_ngau_nhien)
print(f"Đã thêm sublist ngẫu nhiên: {sublist_ngau_nhien}")
print(f"Danh sách sau khi thêm: {List_}")
print("-" * 40)

#4
print("--- Yêu cầu 4: Tính tổng sale value ---")
cac_ngay_can_tinh = ["mon", "tue", "sat", "sun"]
tong_sale = 0
for sublist in List_[:7]: 
    ngay = sublist[0]
    gia_tri = sublist[1]
    
    if ngay in cac_ngay_can_tinh:
        tong_sale += gia_tri

print(f"Tổng sale value của các ngày Thứ 2, Thứ 3, Thứ 7 và Chủ Nhật là: {tong_sale}")