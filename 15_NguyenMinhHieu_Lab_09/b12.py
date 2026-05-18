def them_lau_cho(cho):
   if(cho > 36):
      return None
   ga = 36 - cho
   if(ga*2 + cho*4 == 100):
      return cho
   return them_lau_cho(cho + 1)
print(f"Số con chó có trong bài là: {them_lau_cho(0)}")