ds = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1",'2','3','4','5','6','7','8','9']
staff_list = []
while(True):
   try:
      user_name = input("Nhập username: ")
      if(not user_name):
         raise ValueError("Username không được để trống!")
      user_name = user_name.lower()
      for i in user_name:
         if(i not in ds):
            raise ValueError("Username chứa ký tự không hợp lệ!")
      email = user_name + "@companyname.com"
      staff_list.append(email)
      break
   except Exception as e:
      print(e)
print(staff_list)