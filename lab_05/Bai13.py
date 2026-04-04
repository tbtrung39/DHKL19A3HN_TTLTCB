A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
found = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        # Cắt chuỗi bằng Slicing
        C = A[:i]
        D = A[i:]
        E = B[:j]
        F = B[j:]
        
       
        if int(C) + int(D) == int(E) + int(F):
            print(f"{C}+{D}={E}+{F}")
            found = True
            break 
            
    if found:
        break 

if not found:
    print("Không tồn tại cách đặt!")