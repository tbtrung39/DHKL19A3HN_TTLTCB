List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:")
for item in List_:
    print(item)
target = List_[2][1]
print(f"Phần tử cần tìm: {target}")
print(f"Độ dài của list: {len(List_)}")
List_.append(["special", 200])
print(f"Sau khi thêm sublist mới: {List_}")
days_to_sum = ["mon", "tue", "sat", "sun"]
total_sale = sum(item[1] for item in List_ if item[0] in days_to_sum)
print(f"Tổng sale value (Mon, Tue, Sat, Sun): {total_sale}")