def giai_do_vui(ga, tong_con, tong_chan):
    cho = tong_con - ga
    if ga > tong_con:
        return None
    if (ga * 2 + cho * 4) == tong_chan:
        return ga, cho
    else:
        return giai_do_vui(ga + 1, tong_con, tong_chan)
kq = giai_do_vui(0, 36, 100)
if kq:
    print(f"So ga: {kq[0]}")
    print(f"So cho: {kq[1]}")