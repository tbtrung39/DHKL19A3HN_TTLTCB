input_data = input("Nhập các số tự nhiên, cách nhau bằng dấu cách: ")
lst = [int(x) for x in input_data.split()]
for num in lst:
    assert num % 2 == 0, f"Số {num} là số lẻ, không thỏa mãn điều kiện!"

print("Xác minh thành công: Tất cả các số trong danh sách đều là số chẵn.")
print("Danh sách:", lst)