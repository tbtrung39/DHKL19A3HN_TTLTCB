import datetime as dt
cot_moc = input("Nhập mốc thời gian thứ nhất(dd/mm/yyyy): ")
moc = dt.datetime.strptime(cot_moc, "%d/%m/%Y")
ngay_1 = input("Nhập ngày cần kiểm tra: ")
ngay = dt.datetime.strptime(ngay_1, "%d/%m/%Y")
khoang_cach = ngay - moc
print(khoang_cach)