n = int(input("Nhập số lượng tuple: "))
tuples = []

for i in range(n):
    name = input("Nhập name: ")
    age = int(input("Nhập age: "))
    score = int(input("Nhập score: "))
    t = (name, age, score)
    tuples.append(t)

print("Danh sách tuple ban đầu:")
for i in range(len(tuples)):
    print(tuples[i])

for i in range(len(tuples)):
    for j in range(i + 1, len(tuples)):
        if tuples[i][0] > tuples[j][0]:
            temp = tuples[i]
            tuples[i] = tuples[j]
            tuples[j] = temp
        elif tuples[i][0] == tuples[j][0]:
            if tuples[i][1] > tuples[j][1]:
                temp = tuples[i]
                tuples[i] = tuples[j]
                tuples[j] = temp
            elif tuples[i][1] == tuples[j][1]:
                if tuples[i][2] > tuples[j][2]:
                    temp = tuples[i]
                    tuples[i] = tuples[j]
                    tuples[j] = temp

print("Danh sách tuple sau khi sắp xếp:")
for i in range(len(tuples)):
    print(tuples[i])
