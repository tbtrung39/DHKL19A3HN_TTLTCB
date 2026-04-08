def doc_so_thanh_chu(chuoi_so):
    dict_so = {
        '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
        '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
    }
    ket_qua = [dict_so[s] for s in str(chuoi_so) if s in dict_so]
    return " ".join(ket_qua)

n = input("Nhập một số: ")
print(f"Kết quả: {doc_so_thanh_chu(n)}")