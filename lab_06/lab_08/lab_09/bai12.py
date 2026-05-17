def tim(ga):
    cho = 36 - ga
    if 2 * ga + 4 * cho == 100:
        print("So ga =", ga)
        print("So cho =", cho)
        return
    tim(ga + 1)
tim(0)