a = int(input())
d = {}
for i in range(a):
    n = input()
    d[n] = len(n)
re = sorted(d.items(), key=lambda x: x[1])

for i in range(len(re)):
    print(re[i][0])
## 내코드

import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)


## 정답 코드
#https://velog.io/@1204jh/1181
#https://codechacha.com/ko/python-sort-tuple/
