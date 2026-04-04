Str = input("Nhập đoạn văn bản: ")
word = input("Nhập từ đơn cần tìm: ")

# Hàm split() tự động tách chuỗi theo khoảng trắng
words_list = Str.split()
dem = 0

for w in words_list:
    # Xóa các dấu câu dính kèm để so sánh chính xác từ
    clean_w = w.strip(".,!?()[]{}\"'")
    if clean_w == word:
        dem += 1
        
print("Số lần xuất hiện của từ là:", dem)