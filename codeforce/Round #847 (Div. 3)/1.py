pi = "3141592653589793238462643383279"
a = int(input())
res = []
for i in range(a):
    n = input()
    b = 0
    for j in range(len(n)):
        if n[j] == pi[j]:
            b+=1
        else:
            break
    res.append(b)
for k in range(len(res)):
    print(res[k])