def build_equation (A,B,C,D):
    equation = 'A * (x ** 3) + B * (x ** 2) + C * (x ** 1) + D'
    return equation
def substution (equation,x):
    result = int(eval(equation))
    return result


print('В классическом виде уравнение выглядит следующим образом:\n A * x ^ 3  + B * x ^ 2 + C * x ^ 1 + D = 0')

A= int(input ('Введите A = '))
B= int(input ('Введите B = '))
C= int(input ('Введите C = '))
D= int(input ('Введите D = '))

subs = []
equation = build_equation (A,B,C,D)
for x in range (-100,100,1):
    result = substution(equation,x)
    if result == 0: # Результат записывается только если равен нулю (в правой части всегда стоит "0")
        subs.append(x)

print ('Натуральные корни уравнение = ',subs)


