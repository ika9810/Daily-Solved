t = int(input())
res = []
for i in range(t):
    n = int(input())
    s = list(input())
    while(1):
        if len(s) <= 1:
            res.append(len(s))
            break
        else:
            first = s[0]
            last = s[-1]
            if first == "1" and last == "0":
                s.pop(0)
                s.pop(-1)
            elif first == "0" and last == "1":
                s.pop(0)
                s.pop(-1)
            else:
                res.append(len(s))
                break
for j in range(len(res)):
    print(res[j])