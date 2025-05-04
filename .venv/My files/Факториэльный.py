for a in range (1,10):
    res = a
    sum = 0
    for b in range(a-1,0,-1):
        res = res * b
        sum = sum + res
    print(a, '--',res)
