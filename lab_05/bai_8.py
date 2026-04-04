str = input("Nhap doan van: ")
words = str.split()   #tự động tách theo khoảng trắng
dem = 0
for w in words:
    if len(w.split()) == 1:
        dem += 1
print("So tu don:", dem)