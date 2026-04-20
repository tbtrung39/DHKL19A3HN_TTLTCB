stu_dict = {
    1801 : ["Nguyễn Minh Hiếu", 9.0],
    2804 : ["Tô Văn Giáp", 9.5],
    1105 : ["Hoàng Anh Đức", 8.0]
}
sbd = int(input("Nhập số báo danh cần tra cứu: "))
if(sbd in stu_dict):
    print(stu_dict[sbd])
else:
    print("Không tìm thấy thông tin của sinh viên này!")