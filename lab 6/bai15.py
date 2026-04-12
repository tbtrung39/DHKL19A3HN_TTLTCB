from operator import itemgetter
input_str = input("Nhập các tuple (name, age, score) cách nhau bởi dấu cách: ")
data = []
for item in input_str.split():
    name, age, score = item.split(',')
    data.append((name, int(age), int(score)))
data.sort(key=itemgetter(0, 1, 2))
print("Kết quả sau khi sắp xếp:")
print(data)