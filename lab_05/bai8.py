str = input("Nhap doan van: ")
tu = str.split() 
dem = 0
for w in tu:
    if len(w.split()) == 1:
        dem += 1
print("So tu don:", dem)