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

#b = "𝚌𝚘𝚍𝚎𝚏𝚘𝚛𝚌𝚎𝚜" 라틴어 아스키 코드 문제인줄 알았는데 그냥 알파벳 문제였다..