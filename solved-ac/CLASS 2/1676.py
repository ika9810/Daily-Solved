import math
import sys

input = sys.stdin.readline
a = list(str(math.factorial(int(input()))))
cnt=0
for i in range(1,len(a)+1):
    if a[i*(-1)] == "0":
        cnt+=1
    else:
        print(cnt)
        break