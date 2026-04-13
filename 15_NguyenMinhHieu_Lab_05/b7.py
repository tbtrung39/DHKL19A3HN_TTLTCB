list_ = [["Mon", 73], 
         ["Tue", 89], 
         ["Wed", 95], 
         ["Thu", 103], 
         ["Fri", 115], 
         ["Sat", 128], 
         ["Sum", 120]]
for i in list_:
    print(i)
a = list_[2][1]
print(f"Phần tử thứ 2, thuộc vị trí 3 của danh sách: {a}")
print("Độ dài của danh sách:", len(list_), "\n")
list_.append([1,2,3,4])
print(f"Danh sách sau khi thêm sublist:\n {list_}")
tong = list_[0][1] + list_[1][1] + list_[5][1] + list_[6][1]
print("Tổng của các sale value của thứ 2, 3, 7, CN là:", tong)