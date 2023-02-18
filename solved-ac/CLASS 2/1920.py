import sys
input = sys.stdin.readline

N = int(input())
a = input().split()

for i in range(len(a)):
    if N == a[i]:
        print(1)

# 아직 못품