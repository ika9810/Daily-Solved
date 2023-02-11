import sys
input = sys.stdin.readline

N = int(input())
res = []
prin = []
for _ in range(N):
    a,b = map(int,input().split())
    res.append((a,b))
for j in range(len(res)):
    w = res[j][0]
    h = res[j][1]
    cnt = 0
    for k in range(len(res)):
        if w < res[k][0] and h < res[k][1]:
            cnt += 1
    prin.append(cnt + 1)
for l in range(len(prin)):
    print(prin[l])