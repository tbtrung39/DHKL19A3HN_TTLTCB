ds = []
while True:
    s = input("Nhap name,age,score: ")
    if s == "":
        break
    ten, tuoi, diem = s.split(",")
    ds.append((ten, int(tuoi), int(diem)))
ds.sort(key=lambda x: (x[0], x[1], x[2]))
print(ds)