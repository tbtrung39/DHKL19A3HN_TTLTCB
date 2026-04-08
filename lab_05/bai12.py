import re
str1 = input("Nhập chuỗi Str1: ")
words = re.split(r'[ ,]+', str1)
print("Các từ trong chuỗi là:")
for word in words:
    if word: 
        print(word)