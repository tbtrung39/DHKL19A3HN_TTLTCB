W = input("Nhập chuỗi ký tự: ")

d = {}
for i in range(len(W)):
    if W[i] in d:
        d[W[i]] = d[W[i]] + 1
    else:
        d[W[i]] = 1

print("Dictionary:", d)
