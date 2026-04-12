import re
input_str = input("Nhập danh sách mật khẩu (cách nhau bởi dấu phẩy): ")
passwords = input_str.split(',')
valid_passwords = []
for p in passwords:
    p = p.strip()
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[$#@]", p):
        continue
    valid_passwords.append(p)
print(",".join(valid_passwords))