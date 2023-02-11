import sys
input = sys.stdin.readline

# t = int(input())
# result = []
# for i in range(t):
#     n = int(input())
#     a = input().split("\n")[0].split(" ")
#     res = []
#     for j in range(1,len(a)-1):
#         first = 1
#         second = 1 
#         for k in range(j):
#             first = first * int(a[k])
#         for l in range(j,n):
#             second = second * int(a[l])
#         if first == second:
#             res.append(j)
#     if len(res) == 0:
#         res.append("-1")
#     result.append(res[0])
# for s in range(len(result)):
#     print(result[s])

# Solution of Chatsonic
# def solve_problem(arr, n): 
#     k = -1
#     for i in range(1, n): 
#         mul1 = 1
#         mul2 = 1
#         for j in range(i): 
#             mul1 *= arr[j] 
#         for j in range(i, n): 
#             mul2 *= arr[j] 
#         if (mul1 == mul2): 
#             k = i
#             break
#     return k

# t = int(input())

# for i in range(t):
#     n = int(input()) 
#     arr = list(map(int, input().split()))
#     k = solve_problem(arr, n)
#     print(k)

t = int(input())

for _ in range(t):
    n = int(input()) 
    a = list(map(int, input().split())) 

    k = -1

    for i in range(1, n): 
        left_prod = 1
        right_prod = 1

        for j in range(i): 
            left_prod *= a[j] 
        for j in range(i+1, n): 
            right_prod *= a[j] 

        if left_prod == right_prod: 
            k = i 
            break

    print(k) 