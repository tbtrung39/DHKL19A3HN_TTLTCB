str = input("Nhập một chuỗi gồm chữ và số: ")
str = str.upper()
hex_str = ""
for i in str:
    if(i.isdigit() or (i == "A") or (i == "B") or (i == "C") or (i == "D") or (i == "E") or (i == "F")):
        hex_str += i
print('Chuỗi sau khi lọc là:', hex_str)
print()
j = 0
kq_bin_str = ""
while j < len(hex_str):
    bin_str = ""
    if(hex_str[j] == "0"):
        bin_str += "0000"
    elif(hex_str[j] == "1"):
        bin_str += "0001"
    elif(hex_str[j] == "2"):
        bin_str += "0010"
    elif(hex_str[j] == "3"):
        bin_str += "0011"
    elif(hex_str[j] == "4"):
        bin_str += "0100"
    elif(hex_str[j] == "5"):
        bin_str += "0101"
    elif(hex_str[j] == "6"):
        bin_str += "0110"
    elif(hex_str[j] == "7"):
        bin_str += "0111"
    elif(hex_str[j] == "8"):
        bin_str += "1000"
    elif(hex_str[j] == "9"):
        bin_str += "1001"
    elif(hex_str[j] == "A"):
        bin_str += "1010"
    elif(hex_str[j] == "B"):
        bin_str += "1011"
    elif(hex_str[j] == "C"):
        bin_str += "1100"
    elif(hex_str[j] == "D"):
        bin_str += "1101"
    elif(hex_str[j] == "E"):
        bin_str += "1110"
    elif(hex_str[j] == "F"):
        bin_str += "1111"
    kq_bin_str += bin_str
    j += 1
print(f"Chuỗi HEX {hex_str} sau khi đổi qua dạng nhị phân là: {kq_bin_str}")
print()
kq_dec = 0
for k in range(len(kq_bin_str)):
    kq_dec += int(kq_bin_str[k]) * (2**(len(kq_bin_str) - k - 1))
print("Chuỗi sau khi đổi qua Số thập phân là", kq_dec)