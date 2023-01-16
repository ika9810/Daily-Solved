while(1):
    a = list(input())
    if a[0] == "0":
        break
    b = []
    for i in range(1, len(a)+1):
        b.append(a[-i])
    if a == b:
        print("yes")
    else:
        print("no")