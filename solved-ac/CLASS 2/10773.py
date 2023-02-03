K = int(input())
res = []
for i in range(K):
    a = int(input())
    if a == 0:
        if len(res) <= 0:
            pass
        else:
            res.pop(-1)
    else:
        res.append(a)

result = 0
if len(res) == 0:
    print(0)
else:
    for j in res:
        result += j
    print(result)
    
#reference
#https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9A%94%EC%86%8C-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0