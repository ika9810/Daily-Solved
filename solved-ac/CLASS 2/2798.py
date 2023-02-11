import sys
input = sys.stdin.readline

N,M = map(int, input().split())
card = input().split()
res = []
for i in range(len(card)):
    for j in range(len(card)):
        for k in range(len(card)):
            if len(list(set([i,j,k]))) == 3:
                sum = int(card[i]) + int(card[j]) + int(card[k])
                if sum <= M:
                    res.append(sum)
            else:
                continue
print(max(res))