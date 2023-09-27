# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
# power2n(n-1)+power2n(n-1)
def power2n_a(n):
    if n <  0: return False
    if n == 0: return 1
    if n == 1: return 2
    return power2n_a(n-1) + power2n_a(n-1)

# 方法2b：用遞迴
# 2*power2n(n-1)
def power2n_b(n):
    if n <  0: return False
    if n == 0: return 1
    if n == 1: return 2
    return 2 * power2n_b(n-1)


# 方法 3：用遞迴+查表
# if ....
# power2n(n-1)+power2n(n-1) 
def power2n_3(n):
    if n <  0: return False
    if n == 0: return 