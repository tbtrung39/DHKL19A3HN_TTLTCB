Str1 = input("Nhập chuỗi: ")

Str1_clean = Str1.replace(',', ' ')
words = Str1_clean.split()

for word in words:
    print(word)