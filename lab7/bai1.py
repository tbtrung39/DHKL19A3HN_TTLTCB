tap_hop = set()
while True:
    ky_tu = input("Nhap ky tu (ESC de dung): ")
    if ky_tu == "ESC":
        break
    tap_hop.add(ky_tu)

so_nguyen = set()
for x in tap_hop:
    if x.isdigit():
        so_nguyen.add(x)

for x in so_nguyen:
    tap_hop.discard(x)

print(tap_hop)