def solve_equation():
    A = input("Nhập chuỗi A: ")
    B = input("Nhập chuỗi B: ")

    for i in range(1, len(A)):
        num1 = int(A[:i])
        num2 = int(A[i:])
        sum_A = num1 + num2

        for j in range(1, len(B)):
            num3 = int(B[:j])
            num4 = int(B[j:])
            sum_B = num3 + num4

            if sum_A == sum_B:
                print(f"Đẳng thức đúng: {num1}+{num2}={num3}+{num4}")
                return 
    print("Không tồn tại cách đặt!")
solve_equation()