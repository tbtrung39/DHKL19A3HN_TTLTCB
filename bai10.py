s1 = input("Str1: ")
s2 = input("Str2: ")
max_sub = ""
i = 0
while i < len(s1):
    j = i + 1
    while j <= len(s1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(max_sub):
            max_sub = sub
        j += 1
    i += 1
print("Chuỗi con chung dài nhất:", max_sub)