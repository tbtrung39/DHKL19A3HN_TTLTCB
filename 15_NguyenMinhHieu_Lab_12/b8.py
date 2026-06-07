import datetime as dt
try:
   date = input("Nhập vào ngày tháng năm (dd/mm/yyyy): ")
   ngay_hien_tai = dt.datetime.strptime(date, "%d/%m/%Y")
   ngay_truoc_do = ngay_hien_tai - dt.timedelta(days=1)
   print(f"Ngày trước đó 1 ngày là: {ngay_truoc_do.strftime('%d/%m/%Y')}")
except ValueError:
   print("Lỗi: Bạn đã nhập ngày tháng không tồn tại hoặc sai định dạng!")