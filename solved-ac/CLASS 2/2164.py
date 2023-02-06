# import sys
# N = int(sys.stdin.readline())
# if N == 1:
#     print(1)
# elif N == 2:
#     print(2)
# else:
#     li = []
#     for i in range(N):
#         li.append(i+1)
#     while(1):
#         li.pop(0)
#         if len(li) == 1:
#             print(li[0])
#             break
#         else:
#             a = li[0]

#             li.pop(0)
            
#             li = li + [a]
#시간 초과
input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break
#Reference
#https://tooo1.tistory.com/88