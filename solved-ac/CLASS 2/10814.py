import sys
input = sys.stdin.readline

N = int(input())
res = []
for j in range(N):
    age, name = map(str, input().split())
    res.append((int(age),j,name))
res.sort()
for i in range(len(res)):
    print(res[i][0],res[i][2])