import sys
def solution(n):
    number = [n]
    answer = []
    while True:
        answer.append(number.copy())
        temp = number.pop()
        if temp != 1:
            number.append(temp - 1)
            number.append(1)
        else:
            sum = 2
            for _ in range(len(number)):
                if number and number[-1] == 1:
                    sum += 1
                    number.pop()
            if not number:
                break
            pivot = number.pop() - 1
            number.append(pivot)
            while sum > pivot:
                number.append(pivot)
                sum -= pivot
            number.append(sum)
    return answer
a = int(sys.stdin.readline())
res = []
for i in range(a):
    n,s,r = map(int, sys.stdin.readline().split())
    high = s-r
    b = solution(r)
    for j in range(len(b)):
        if len(b[j]) == n-1:
            res.append(b[j])
            #print(b[j])
    res[0].append(high)
    if len(res) == 1:
        res[0].sort()
        print(*res[0])
    else:
        for k in range(len(res)):
            for l in range(len(res[k])):
                if res[k][l] > high:
                    res.remove(res[k])

        print(*res[0])
#https://maximum-curry30.tistory.com/281
#https://yeomss.tistory.com/160