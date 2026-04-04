str1 = input("Nhập một chuỗi ký tự: ")
chuoi_moi = ""
for i in str1:
    if(i != " " or i != "," or i != "."):
        chuoi_moi += i
    if(i == " "):
        chuoi_moi += "\n"
    if(i == "," or i == "."):
        chuoi_moi = chuoi_moi.replace(i, "")
print(chuoi_moi)