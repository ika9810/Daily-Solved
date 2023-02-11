#Correct Code
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
#Wrong Code of Mine
import sys
input = sys.stdin.readline
res = []
a,b = map(int, input().split())

def lcm(a,b):
    if a>b:
        for i in range(b):
            if a%(b-i) == 0:
                if b%(b-i) == 0:
                    return b-i
                else:
                    pass
            else:
                pass
    elif b>a:
        for i in range(a):
            if b%(a-i) == 0:
                if a%(a-i) == 0:
                    return a-i

                else:
                    pass
            else:
                pass
def gdb(a,b):
    if a>b:
        for i in range(a,10001):
            if i%a == 0:
                if i % b == 0:
                    return i
                    res.append(i)
                    break
                else:
                    pass
            else:
                pass
    elif b>a:
        for i in range(b,10001):
            if i%b == 0:
                if i % a == 0:
                    return i
                    res.append(i)
                    break
                else:
                    pass
            else:
                pass
print(lcm(a,b))
print(gdb(a,b))

#Reference
#https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-2609-Python-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98