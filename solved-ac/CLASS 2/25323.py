import math
n = int(input())
s = list(map(int,input().split()))
an = s.copy()
s.sort()
e=0
for i in range(n):
    if int(math.isqrt(s[i]*an[i]))**2==s[i]*an[i]:
        pass
    else:
        e =1
        break
if e==1:
    print("NO")
else:
    print("YES")

#Reference
#https://77dptjd.tistory.com/2