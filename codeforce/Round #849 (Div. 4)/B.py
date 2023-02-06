t = int(input())

def move(msg,x,y):
    X = {}
    Y = {}
    if msg == "L":
        x += -1
        return [x,y]
    elif msg == "R":
        x += 1
        return [x,y]
    elif msg == "U":
        y += 1
        return [x,y]
    elif msg == "D":
        y += -1
        return [x,y]

result = []

for i in range(t):
    n = int(input())
    s = list(input())

    pos = {}
    pos["x"] = 0
    pos["y"] = 0

    check = False
    for j in s:
        # print("here",pos["x"],pos["y"])
        res = move(j,pos["x"],pos["y"])
        pos["x"] = res[0]
        pos["y"] = res[1]
        if pos["x"] == 1:
            if pos["y"] == 1:
                #print("YES")
                result.append("YES")
                check = True
                break
            else:
                pass
        else:
            pass
    if check:
        continue
    else:
        #print("NO")
        result.append("NO")
        continue

for k in range(len(result)):
    print(result[k])