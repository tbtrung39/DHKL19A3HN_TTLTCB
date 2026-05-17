list1 = list(map(int, input("Nhập list1 (các số cách nhau bằng dấu cách): ").split()))
list2 = list(map(int, input("Nhập list2 (các số cách nhau bằng dấu cách): ").split()))

d = {}
for i in range(len(list1)):
    d[list1[i]] = list2[i]

print("Dictionary:")
for key in d:
    print(str(key) + ": " + str(d[key]))
