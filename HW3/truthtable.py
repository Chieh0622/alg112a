def truthtable(n, current_table=[]):
    if n == 0:
        print(current_table) 
    else:
        for value in [0, 1]:
            truthtable(n - 1, current_table + [value])

n = int(input('enter number:'))
truthtable(n)