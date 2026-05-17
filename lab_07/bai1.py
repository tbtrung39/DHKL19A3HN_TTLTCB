s = set()
x = input("Nhập phần tử (nhập 'ESC' để dừng): ")
while x != "ESC":
    s.add(x)
    x = input("Nhập phần tử (nhập 'ESC' để dừng): ")

print("Set:", s)
print("Số phần tử:", len(s))
