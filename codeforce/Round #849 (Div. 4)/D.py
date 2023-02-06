import sys
t = int(sys.stdin.readline())

result = []

for i in range(t):
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline().strip())
    res = []
    for j in range(0,len(s)-1):
        a = len(list(set(s[:j+1])))
        b = len(list(set(s[j+1:])))
        #print(list(set(s[:j+1])),list(set(s[j+1:])))
        c = a + b
        res.append(c)

    result.append(max(res))
for j in range(len(result)):
    print(result[j])
#Time limit exceeded on test 3 시간초과로 sol 실패