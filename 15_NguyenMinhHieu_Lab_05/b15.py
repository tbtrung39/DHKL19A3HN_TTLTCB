data = []
while True:
    line = input("Nhập: ")
    if not line:
        break
    parts = line.split(",")
    name = parts[0].strip()
    age = int(parts[1].strip())
    score = int(parts[2].strip())
    data.append((name, age, score))
data.sort(key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sách sau khi sắp xếp:")
for item in data:
    print(item)