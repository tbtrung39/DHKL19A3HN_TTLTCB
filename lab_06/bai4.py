lst = []
while True:
    n = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if n == 0:
        break
    lst.append(n)

print(f"Danh sách ban đầu: {lst}")

sub = [1, 2, 3]
lst = sub + lst 
lst[4:4] = sub 
lst.extend(sub)
print(f"Sau khi chèn: {lst}")

k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(lst):
    lst.pop(k)
    print(f"Sau khi xóa vị trí {k}: {lst}")
else:
    print("Vị trí không hợp lệ.")

lst.sort()
print(f"Tăng dần: {lst}")
lst.sort(reverse=True)
print(f"Giảm dần: {lst}")