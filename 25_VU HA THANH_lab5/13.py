def solve():
    a_str = input("Nhập chuỗi A: ")
    b_str = input("Nhập chuỗi B: ")

    found = False
    for i in range(1, len(a_str)):
        c_str = a_str[:i] 
        d_str = a_str[i:] 
        
        c = int(c_str)
        d = int(d_str)
        for j in range(1, len(b_str)):
            e_str = b_str[:j]
            f_str = b_str[j:]
            
            e = int(e_str)
            f = int(f_str)
            if c + d == e + f:
                print(f"Kết quả: {c} + {d} = {e} + {f}")
                found = True
                return 

    if not found:
        print("Không tồn tại cách đặt!")
solve()