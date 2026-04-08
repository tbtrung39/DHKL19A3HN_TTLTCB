text = input("Nhập đoạn văn bản: ")
word_to_find = input("Nhập từ đơn cần tìm: ")

words = text.split()
count = words.count(word_to_find)

print(f"Từ '{word_to_find}' xuất hiện {count} lần.")