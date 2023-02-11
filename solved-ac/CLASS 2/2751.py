import sys
input = sys.stdin.readline
res = []
N = int(input())
for _ in range(N):
    res.append(int(input()))
for i in sorted(res):
    print(i)
# 내 코드
# 틀렸습니다 판정 받음
# 정답 확안하니 콜롬버스 달걀 처럼 너무 허무하다. sorted 사용하는 문제
# import sys
# input = sys.stdin.readline

# arr = [0]*1000000
# minus = [0]*1000000
# zero = [0]

# N = int(input())
# for _ in range(N):
#     a = int(input())
#     if a < 0:
#         minus[abs(a)-1] += 1
#     elif a > 0:
#         arr[a-1] += 1
#     elif a == 0:
#         zero[0] += 1
# for i in range(len(minus)):
#     for j in range(minus[i]):
#         print((i+1)*-1)

# for z in range(zero[0]):
#     print(0)

# for k in range(len(arr)):
#     for l in range(arr[k]):
#         print((k+1))