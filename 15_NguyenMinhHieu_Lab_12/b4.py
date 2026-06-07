name = input("Nhập tên file muốn mở (kèm đuôi): ")
try:
   with open(name, 'r', encoding='utf-8') as file:
      assert file.readable(), 'file đang mở sai chế độ!'
      content = file.readlines()
   another_name = input("Nhập tên file muốn ghi nội dung vào: ")
   with open(another_name, 'w', encoding='utf-8') as file:
      file.write(content)
except FileNotFoundError:
   print("Không tìm thấy file!")
except Exception as e:
   print(e)