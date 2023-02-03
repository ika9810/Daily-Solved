a, b = map(int, input().split())
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
c = factorial(a)
d = factorial(a-b) * factorial(b)
print(int(c/d))
#n!
#(n-k)!k!
#reference
#https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
