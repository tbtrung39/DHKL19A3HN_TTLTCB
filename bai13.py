A = input("A: ")
B = input("B: ")
found = False
i = 1
while i < len(A):
    C = int(A[:i])
    D = int(A[i:])
    j = 1
    while j < len(B):
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(str(C)+"+"+str(D)+"="+str(E)+"+"+str(F))
            found = True
        j += 1
    i += 1
if not found:
    print("Khong ton tai cach dat!")