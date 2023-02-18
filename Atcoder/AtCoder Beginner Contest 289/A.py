import sys
input = sys.stdin.readline

arr = [0]*10
s = input().split("\n")[0]

for i in range(len(s)):
    if int(s[i]) != 1:
        arr[i] = 1
print("".join(list(map(str,arr[:len(s)]))))
#https://blockdmask.tistory.com/581
#flip
#https://coding-groot.tistory.com/22
# 리스트 형변환