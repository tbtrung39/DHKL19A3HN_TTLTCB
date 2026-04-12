input_str = input("Nhập X, Y (cách nhau bởi dấu phẩy): ")
dimensions = [int(x) for x in input_str.split(',')]
X, Y = dimensions[0], dimensions[1]
multilist = [[i * j for j in range(Y)] for i in range(X)]
print(multilist)