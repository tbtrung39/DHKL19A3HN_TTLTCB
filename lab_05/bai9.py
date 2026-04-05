s = input("Nhap chuoi Str: ")
if len(s) == 0:
    print("Chuoi rong")
else:
    max_sub = ""
    tam = s[0]
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            tam += s[i]
        else:
            if len(tam) > len(max_sub):
                max_sub = tam
            tam = s[i]
    if len(tam) > len(max_sub):
        max_sub = tam
        print("Chuoi con lap lai dai nhat la:", max_sub)