def truthtable(n, current_table=[]):
    if n == 0:
        print(current_table) 
    else:
        for value in [0, 1, 2]:
            truthtable(n - 1, current_table + [value])

truthtable(int(input("enter number : ")))