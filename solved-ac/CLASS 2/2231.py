import sys
input = sys.stdin.readline

N = int(input())
chk = True
for i in range(1,N):
    c = 0
    for j in range(len(str(i))):
        c += int(str(i)[j])
    i += c
    if i == N:
        print(i-c)
        chk = False
        break
if chk:
    print(0)