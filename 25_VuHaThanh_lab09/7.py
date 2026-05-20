def find_solutions(N, n, current_combination=[]):
    if len(current_combination) == n:
        if N == 0:  
            print(current_combination)
        return

    for i in range(N + 1):
        find_solutions(N - i, n, current_combination + [i])

if __name__ == "__main__":
    N = int(input("Nhập tổng N: "))
    n = int(input("Nhập số lượng ẩn n: "))

    print(f"Các bộ nghiệm tự nhiên của phương trình:")
    find_solutions(N, n)