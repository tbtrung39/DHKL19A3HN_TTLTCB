A = input("Nhập A: ")
B = input("Nhập B: ")
tim = False
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print(C, "+", D, "=", E, "+", F)
            tim = True
            break
    if tim:
        break
if tim == False:
    print("Không tồn tại cách đặt!")