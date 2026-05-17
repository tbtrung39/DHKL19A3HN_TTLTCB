def giai_do(g, c):
    if g + c == 36 and 2 * g + 4 * c == 100:
        print("Số gà:", g)
        print("Số chó:", c)
        return
    giai_do(g - 1, c + 1)
giai_do(36, 0)