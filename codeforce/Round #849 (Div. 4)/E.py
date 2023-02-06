t = int(input())

for i in range(t):
    res = []
    n = int(input())
    s = input().split(' ')
    for k in range(len(s)):
        s[k] = int(s[k])
    print("her",sum(s))
    res.append(sum(s))
    for j in range(len(s)-1):
        s[j] = -1 * s[j]
        s[j+1] = -1 * s[j+1]
        print("here",s, sum(s))
        ss= sum(s)
        res.append(ss)
    print(res)
    print(max(res))

    #미완성 not completed