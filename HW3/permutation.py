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

permutation(int(input("enter number : ")))