for a in range(1,10000):
    divs = [0, ]
    for b in range(a-1,0,-1):
         c = a%b #Возвращает остаток от деления - если он равен 0, то число заносимтся в список делителей.
         if c == 0:
              divs.append(b)
    summ = 0
    for d in divs:
        summ = summ + d
    if summ == a:
        print(a,' - Совершенное число')

for a in range(33550330,33550340):
    divs = [0, ]
    for b in range(a-1,0,-1):
         c = a%b #Возвращает остаток от деления - если он равен 0, то число заносимтся в список делителей.
         if c == 0:
              divs.append(b)
    summ = 0
    for d in divs:
        summ = summ + d
    if summ == a:
        print(a,' - Совершенное число')