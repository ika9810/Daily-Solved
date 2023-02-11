import sys
input = sys.stdin.readline

N = int(input())
d= []
for i in range(N):
    x, y = map(int,input().split())
    d.append((y,x))

d.sort(key=lambda x:(x[0],x[1]))

for j in range(len(d)):
    tur = d[j]
    print(tur[1], tur[0])
#Reference
#정렬 방식
#https://leedakyeong.tistory.com/entry/python-%ED%8A%9C%ED%94%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%EB%91%90-%EB%B2%88%EC%A7%B8-%EC%9B%90%EC%86%8C%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-tuple-sorting-in-python
#인풋 방식
#https://wook-2124.tistory.com/473