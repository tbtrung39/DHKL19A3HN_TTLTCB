password = input("Nhập mật khẩu: ")

co_chu_thuong = False
co_so = False
co_chu_hoa = False
co_ky_tu_dac_biet = False
do_dai_hop_le = False

for i in range(len(password)):
    if password[i] >= 'a' and password[i] <= 'z':
        co_chu_thuong = True
    elif password[i] >= '0' and password[i] <= '9':
        co_so = True
    elif password[i] >= 'A' and password[i] <= 'Z':
        co_chu_hoa = True
    elif password[i] == '$' or password[i] == '#' or password[i] == '@':
        co_ky_tu_dac_biet = True

if len(password) >= 6 and len(password) <= 12:
    do_dai_hop_le = True

if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_dac_biet and do_dai_hop_le:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")
    if not co_chu_thuong:
        print("- Thiếu chữ cái thường [a-z]")
    if not co_so:
        print("- Thiếu số [0-9]")
    if not co_chu_hoa:
        print("- Thiếu chữ cái hoa [A-Z]")
    if not co_ky_tu_dac_biet:
        print("- Thiếu ký tự đặc biệt [$ # @]")
    if not do_dai_hop_le:
        print("- Độ dài phải từ 6 đến 12 ký tự")
