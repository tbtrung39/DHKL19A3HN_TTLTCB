ds = input("Nhap mat khau: ").split(",")
hop_le = []
for mk in ds:
    if (6 <= len(mk) <= 12 and
        any(c.islower() for c in mk) and
        any(c.isupper() for c in mk) and
        any(c.isdigit() for c in mk) and
        any(c in "$#@" for c in mk)):
        hop_le.append(mk)
print(",".join(hop_le))