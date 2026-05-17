d = {}
for i in range(1, 101):
    binary = bin(i)[2:]
    d[i] = binary

print("Dictionary (100 số và chuỗi nhị phân):")
for key in sorted(d.keys()):
    print(str(key) + ": " + d[key])
