import random as rd
while(True):
    num = [i for i in range(201) if(i % 5 == 0 and i % 7 == 0)]
    break
if(num):
    random_num = rd.choice(num)
    print(random_num)