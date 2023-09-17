n = int(input('Enter number:'))
fib = []

def fib(n):
    fib = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range (2, n+1):
            fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print(f'fib({n}) = {fib(n)}')