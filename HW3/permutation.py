# 參考 https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/02a-%E5%88%97%E8%88%89%E6%B3%95/03-permutation/permutation.py

def permutation(n):
    perm = []
    return permNext(n, perm)

def permNext(n, perm):
    if len(perm) == n:
        print(perm)
        return
    else:
        for x in range(n):
            if x not in perm:
                perm.append(x)
                permNext(n, perm)
                perm.pop()

n = int(input('enter number:'))
permutation(n)