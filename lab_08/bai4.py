def tim_uoc_so(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("Nhập n: "))
uoc_so = tim_uoc_so(n)
print(f"Các ước số của {n}: {uoc_so}")
