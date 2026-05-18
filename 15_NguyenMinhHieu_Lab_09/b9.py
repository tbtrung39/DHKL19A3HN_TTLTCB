import sys
def dao_chuoi_de_quy():
   ky_tu = sys.stdin.read(1)
   if ky_tu == "\n":
      return
   dao_chuoi_de_quy()
   sys.stdout.write(ky_tu)
   sys.stdout.flush()
print(dao_chuoi_de_quy())