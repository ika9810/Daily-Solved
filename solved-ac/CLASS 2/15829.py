import sys
input = sys.stdin.readline
L = int(input())
s = list(input())
s.pop(-1)

res = 0
for i in range(len(s)):
    res += (ord(s[i])-96)*(31**i)
print(res % 1234567891)