def tim(g, c):
    if g + c == 36 and 2 * g + 4 * c == 100:
        print("Số gà:", g)
        print("Số chó:", c)
        return
    if g > 36:
        return
    tim(g + 1, 36 - (g + 1))
tim(0, 36)