def num_squares_hitro50 (number):
   print('Число сотен = ' , 25 + (number-50))
   print('Число Единиц =  ', (50 - number) * (50 - number))
   result = 2500 + (number - 50) * 100 + (number - 50) * (number - 50)
   print('Итоговоая сумма = ', result)

def num_squares_hitro100 (number):
   print('Число сотен = ' , 100 + 2 * (number-100))
   print('Число Единиц =  ', (100 - number) * (100 - number))
   result = 10000 + (number - 100) * 100 + (number - 100) * (number - 100)
   print('Итоговоая сумма = ', result)

def num_squares(num_des ):
   first_square = num_des * num_des
   squqare = num_des  * num_des
   next_square = 0
   print(num_des , ' - ', squqare)  # Первая строка для десятка
   for number in range(num_des  + 1, num_des  + 10, 1):
       print(number, ' - ', end=' ')  # Сама цифра
       next_square = number * number
       print(next_square)

while True:
    result = 0
    number = int(input('Введи число от 26 до 124\n'))
    num_des = number // 10 * 10
    if number > 25 and  number <75:
        print('Число меньше 75\n')
        num_squares_hitro50(number)
        print('------Квадраты для проверки------')
        num_squares(num_des)
    elif number > 75 and number < 125:
        print('Число больше 75\n')
        num_squares_hitro100(number)
        print('------Квадраты для проверки------')
        num_squares(num_des)
    else:
        print()





