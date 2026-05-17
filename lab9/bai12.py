def tim_ga_cho(index=0, ga=None, cho=None):
    if ga is None:
        ga = []
    if cho is None:
        cho = []
    
    if index == 36:
        for g in range(37):
            c = 36 - g
            if g + c == 36 and 2 * g + 4 * c == 100:
                return g, c
        return None, None
    
    return None, None

def solve_ga_cho():
    for g in range(37):
        c = 36 - g
        if 2 * g + 4 * c == 100:
            return g, c
    return None, None

ga, cho = solve_ga_cho()

if ga is not None and cho is not None:
    print("Bài toán: Vừa gà vừa chó - Bó lại cho tròn")
    print(f"36 con - 100 chân")
    print(f"Số gà: {ga} con")
    print(f"Số chó: {cho} con")
    print(f"Kiểm tra: {ga} + {cho} = {ga + cho} con")
    print(f"Kiểm tra: {2 * ga} + {4 * cho} = {2 * ga + 4 * cho} chân")
else:
    print("Không tìm được lời giải")
