# Bài 10
num = input("Nhập số thập phân: ")
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
while i < len(num):
    if num[i] == '.':
        print("phẩy", end=" ")
    else:
        print(chu_so[int(num[i])], end=" ")
    i += 1