a = "codeforces"
b = "codeforces"

li = []
for i in range(len(a)):
    li.append(ord(b[i]))
res = []
t = int(input())
for i in range(t):
    c = ord(input())
    if c in li:
        res.append("YES")
    else:
        res.append("NO")
for j in range(len(res)):
    print(res[j])

#b = "ππππππππππ" λΌν΄μ΄ μμ€ν€ μ½λ λ¬Έμ μΈμ€ μμλλ° κ·Έλ₯ μνλ²³ λ¬Έμ μλ€..