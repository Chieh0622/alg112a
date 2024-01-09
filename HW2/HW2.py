# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
# power2n(n-1)+power2n(n-1)
def power2n_a(n):
    if n == 0: return 1
    return power2n_a(n - 1) + power2n_a(n - 1)

# 方法2b：用遞迴
# 2*power2n(n-1)
def power2n_b(n):
    if n == 0: return 1
    return 2 * power2n_b(n-1)

#方法 3：用遞迴+查表
# if ....
# power2n(n-1)+power2n(n-1)
fib = [None] * 10000
fib[0] = 1
def power2n_c(n):
    if n <  0: return False
    if not fib[n] is None: return fib[n]
    fib[n] = power2n_c(n-1) + power2n_c(n-1)
    return fib[n]

n = int(input('Please enter a number: '))

print(f'power2n({n})   = {power2n(n)}')
print(f'power2n_a({n}) = {power2n_a(n)}')
print(f'power2n_b({n}) = {power2n_b(n)}')
print(f'power2n_c({n}) = {power2n_c(n)}')