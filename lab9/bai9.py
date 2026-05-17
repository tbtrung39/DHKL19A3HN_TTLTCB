def dao_nguoc_so(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(dao_nguoc_so(n // 10)))

num = int(input("Nhập một số nguyên dương: "))
ket_qua = dao_nguoc_so(num)

print(f"Số {num} đảo ngược là: {ket_qua}")
