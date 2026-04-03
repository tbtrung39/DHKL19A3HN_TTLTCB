n = input("Nhap so: ")

i = 0
while i < len(n):
    if n[i] == '0':
        print("khong", end=" ")
    elif n[i] == '1':
        print("mot", end=" ")
    elif n[i] == '2':
        print("hai", end=" ")
    elif n[i] == '3':
        print("ba", end=" ")
    elif n[i] == '4':
        print("bon", end=" ")
    elif n[i] == '5':
        print("nam", end=" ")
    elif n[i] == '6':
        print("sau", end=" ")
    elif n[i] == '7':
        print("bay", end=" ")
    elif n[i] == '8':
        print("tam", end=" ")
    elif n[i] == '9':
        print("chin", end=" ")
    i = i + 1