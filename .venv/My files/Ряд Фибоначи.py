def fiabanachi (n):
    fib = [0,1,]
    while True:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        if len(fib) > n: #Ограничение выборки
            print(fib)
            break

fiabanachi(6)