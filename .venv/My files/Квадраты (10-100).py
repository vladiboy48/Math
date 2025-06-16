import matplotlib.pyplot
def num_squares (num):
    square = num * num
    first_square = square
    next_square = 0
    print (num,' - ',square) # Первая строка для десятка
    for number in range (num+1,num+10,1):
        numbers_list.append(number)
        print(number,' - ',end=' ')  # Само число
        next_square = number * number
        squqares_list.append(next_square)
        print (next_square,' - ',(next_square-square),' - ',end=' ') # Квадрат и Локальная разность
        local_diffs_list.append(next_square-square)
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

# Cоздаётся 2D линия (Передаём в значения в координатные плоскости)
matplotlib.pyplot.plot(numbers_list,squqares_list)
matplotlib.pyplot.plot(numbers_list,local_diffs_list)
matplotlib.pyplot.plot(numbers_list,accum_diffs_list)

# Оформление графика
matplotlib.pyplot.grid(True) #Сетка
matplotlib.pyplot.legend(['График,квадратов','Локальная разность', 'Накопленная разность'],loc = 1) #Легенда
matplotlib.pyplot.title("График функции y=x^2", color='green', fontsize = 20, fontname='Tahoma' ) # Название самого графика
matplotlib.pyplot.xlabel("Число(х)", color='red', fontsize = 18) # X
matplotlib.pyplot.ylabel("Квадрат числа(у)", color='red', fontsize = 18); # Y
matplotlib.pyplot.axis([10, 100, 100, 3000]) # [xmin, xmax, ymin, ymax]
matplotlib.pyplot.text(15,2500,'Добрый день!',fontsize=14, bbox={'facecolor':'yellow','alpha':0.2})
matplotlib.pyplot.show() # Отображение графика в отдельном окне.