import sys
input = sys.stdin.readline

num = int(input())
arr = [0]*10000
c = []
for i in range(num):
    b = int(input())
    arr[b-1] += 1
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
            
#Reference
#https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC