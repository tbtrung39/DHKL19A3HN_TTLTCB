ds_a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ds_b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ds_c = []
ds_d = ["$", "#", "@"]
for tl in ds_a:
    tl = tl.upper()
    ds_c.append(tl)
while(True):
    mk = input("Nhập danh sách mật khẩu cần thử(cách nhau bằng dấu phẩy): ")
    ds_mk = mk.split(",")
    print("Danh sách mật khẩu là: ", ds_mk)
    for password in ds_mk:
            password = password.strip()
            co_chu_thuong = False
            co_chu_hoa = False
            co_so = False
            co_ky_tu_db = False
            for i in password:
                if i in ds_a: co_chu_thuong = True
                if i in ds_c: co_chu_hoa = True
                if i in ds_b: co_so = True
                if i in ds_d: co_ky_tu_db = True
            if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db:
                print(f"Mật khẩu đủ điều kiện là: {password}")
                break
            else:
                print("Không có mật khẩu hợp lệ!")
    break
