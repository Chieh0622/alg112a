# 參考 https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/02c-%E6%9A%B4%E5%8A%9B%E6%B3%95/solve/bruteForce1.py

# x^2 - 3x + 1 = 0

import math
from numpy import arange
def solution(n):
    ans = n**2 - 3*n +1
    return ans
for i in arange(-100,100,0.001):
    if abs(solution(i)) < 0.001:
        print("x=", i, " f(x)=", solution(i))