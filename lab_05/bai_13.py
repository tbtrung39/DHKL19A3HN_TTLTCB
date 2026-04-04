A = input("Nhap A: ")
B = input("Nhap B: ")
found = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])  
        if C + D == E + F:
            print(str(C) + "+" + str(D) + "=" + str(E) + "+" + str(F))
            found = True
if not found:
    print("Khong ton tai cach dat!")