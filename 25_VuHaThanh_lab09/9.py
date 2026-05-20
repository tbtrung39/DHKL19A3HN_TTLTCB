def dao_nguoc_in(n):
    if n < 10:
        print(n, end="")
        return
    
    print(n % 10, end="")
    
    dao_nguoc_in(n // 10)
print("Kết quả cách 1: ", end="")
dao_nguoc_in(12345)  
print()