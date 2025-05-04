import pprint

def equation (a,b,n,c):

    def paskal_triangle(quanity_lines):
        old_string = []
        new_string = []
        paskal_matrix = {}
        for coord_x in range(0, quanity_lines + 2, 1):  # формируем первую строку вручную
            if coord_x == 1:
                old_string.append(1)
            else:
                old_string.append(0)
        paskal_matrix[0] = old_string  # Запись нулевого элемента в матрицу
        for coord_y in range(1, quanity_lines, 1):
            new_string = [0]
            for coord_x in range(1, quanity_lines + 2, 1):
                new_string.append(old_string[coord_x - 1] + old_string[coord_x])
            old_string = new_string  # Формируемая строка становиться существующей
            paskal_matrix[coord_y] = old_string
        return paskal_matrix

    def equation_members (a,b,n,d,paskal_matrix): #Просто печатает члены отдельно
        print('Члены уравнения выглядят следующим образом:')
        string = (paskal_matrix)[n]  # Идентифицируем строку с нужными коэффицентами
        string = string[1:n + 2]  # Убираем нули из строки через Срез
        equation_matrix = {}  # Матрица с членами уравнения
        index_in_matrix = 0

        while n > d:
            for binom_coef in string:
                member = ("""(%s * ((%s * x) ** %s)) * (%s ** %s)""" % (binom_coef,a,n,b,d))
                n -= 1
                d += 1
                index_in_matrix += 1
                equation_matrix[index_in_matrix] = member
        pprint.pprint(equation_matrix)
        return equation_matrix


    def ident_final_equation (equation_matrix,c): # Получаем итоговое уравнение
        indexs = equation_matrix.keys()
        final_equation = '' #Пустая строка
        print('\nУравнение в развернутом виде имеет вид:')
        for index_in_matrix in indexs:
            local_member = equation_matrix[index_in_matrix]
            final_equation = (final_equation + local_member + ' + ')
        final_equation = final_equation + '0' #Костыль чтобы завершить левую часть
        print (final_equation, ' = %s' %(c))  #Подстановка правой части
        return final_equation

    def tvar(final_equation, x):
        result = int(eval(final_equation))
        return result

    d = 0  # Переменна для степени свободного члена
    print("""Уравнение выглядит следующим образом:\n( %s * x + %s) ^ %s = %s\n""" % (a, b, n, c))
    paskal_matrix = paskal_triangle(n+1)
    equation_matrix = (equation_members(a,b,n, d, paskal_matrix))  #Ф
    final_equation = ident_final_equation(equation_matrix,c)

    for x in range(-100, 100, 1):
        result = tvar(final_equation, x)
        if result == c:
            subs.append(x)
    print('\nНатуральные корни ураненения = ',subs)




# print('Формула вида (a * X + b)^n' = c)
# a = input('Введите а (коэффециент при Х) = ')
# b = input('Введите b (свободный член) = ')
# n = input('Введите n (степень) = ')
# n = input('Введите c (число после =) = ')
a = 1
b = 5
n = 3
c = 343
subs = []
equation (a,b,n,c)



