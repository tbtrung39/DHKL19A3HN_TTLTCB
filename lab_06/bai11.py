n = int(input())
A = list(map(int, input().split()))

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
C = [x*x for x in A]

import random
D = random.sample([x for x in A if x % 3 == 0], k=min(3,len(A)))

print(B)
print(C)
print(D)