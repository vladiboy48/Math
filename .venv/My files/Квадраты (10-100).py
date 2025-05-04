import matplotlib.pyplot
def num_squares (num):
    first_square = num * num
    squqare = num * num
    next_square = 0
    print (num,' - ',squqare) # Первая строка для десятка
    for number in range (num+1,num+10,1):
        numbers_list.append(number)
        print(number,' - ',end=' ')  # Сама цифра
        next_square = number * number
        squqares_list.append(next_square)
        print (next_square,' - ',(next_square-squqare),' - ',end=' ') # Локальная разность
        local_diffs_list.append(next_square-squqare)
        print(next_square - first_square) # Накопленная разность
        accum_diffs_list.append(next_square - first_square)
        squqare = next_square
    print('--------------------------')

numbers_list = []
squqares_list = []
local_diffs_list = []
accum_diffs_list = []

for number in range (10,100,10):
    num_squares(number)


# Тут уже создаётся объект 2D линии (Передаём в значения в координатные плоскости)
matplotlib.pyplot.plot(numbers_list,squqares_list)
matplotlib.pyplot.plot(numbers_list,local_diffs_list)
matplotlib.pyplot.plot(numbers_list,accum_diffs_list)

#Наводим красоту
matplotlib.pyplot.grid(True) #Сетка
matplotlib.pyplot.legend(['График,квадратов','Локальная разность', 'Накопленная разность'],loc = 1) #Головач, двойка это позиция её отображения.
matplotlib.pyplot.title("Грвфик функции y=x^2", color='green', fontsize = 20, fontname='Tahoma' ) # Название самого графика
matplotlib.pyplot.xlabel("Число(х)", color='red', fontsize = 18) # Название икса
matplotlib.pyplot.ylabel("Квадрат числа(у)", color='red', fontsize = 18); # Название игрика
matplotlib.pyplot.axis([10, 100, 100, 3000]) # [xmin, xmax, ymin, ymax]
matplotlib.pyplot.text(15,2500,'Добрый день',fontsize=14, bbox={'facecolor':'yellow','alpha':0.2})


matplotlib.pyplot.show() # Тут мы чисто его отображаем в виде plotting window