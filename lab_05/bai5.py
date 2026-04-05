Str = input("Nhập chuỗi: ")
chuoi_so = ""
for c in Str:
    if c.isdigit():
        chuoi_so += c
if chuoi_so == "":
    print("Không có ký tự số nào trong chuỗi.")
else:
    so = int(chuoi_so)
    print(f"Chuỗi số giữ lại: {so}")
    if so > 1:
        tong_uoc = 0
        for i in range(1, so):
            if so % i == 0:
                tong_uoc += i
        if tong_uoc == so:
            print(f"{so} là số hoàn hảo.")
        else:
            print(f"{so} không phải là số hoàn hảo.")
    else:
        print(f"{so} không phải là số hoàn hảo.")