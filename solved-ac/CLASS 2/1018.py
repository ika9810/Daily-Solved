import sys
input = sys.stdin.readline

M, N = map(int, input().split())
res = []
for _ in range(M):
    a = list(input())
    res.append(a)
cnt = 0
for i in range(len(res)):
    for j in range(len(res[i])-1):
        if res[i][j] == "B":
            if res[i][j+1] == "B":
                cnt += 1
                res[i][j+1] = "W"
        elif res[i][j] == "W":
            if res[i][j+1] == "W":
                cnt += 1
                res[i][j+1] = "B"
print(cnt)

#문제를 잘못 이해 아직 못품