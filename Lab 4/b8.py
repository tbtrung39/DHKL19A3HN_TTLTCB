# Bài 8
char = input("Nhập một ký tự: ")
while len(char) != 1:
    print("Bạn phải nhập đúng 1 ký tự.")
    char = input("Nhập lại một ký tự: ")
print("Giá trị ASCII của ký tự", char, "là:", )
