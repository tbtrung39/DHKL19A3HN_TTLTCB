# Bài 6
num = input("Nhập một số: ")
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
while i < len(num):
    print(chu_so[int(num[i])], end=" ")
    i += 1