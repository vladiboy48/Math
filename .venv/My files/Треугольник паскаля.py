import time

def paskal_triangle(quanity_lines):
    def global_check(matrix):

        def check_sum(line):
            summ = 0
            for element in line:
                summ = summ + element
            time.sleep(0.5)
            print(' Сумма = ', summ, end=' : ')

        def check_triangle(coord_y, matrix):
            coord_x = coord_y - 1
            time.sleep(0.5)
            print(' Треугольное = ', matrix[coord_y][coord_x], end=' : ')

        def check_fib(coord_y, matrix):
            coord_x = 1
            fib_sum = 0
            for coord_y_local in range(coord_y, 0, -1):
                fib_sum = fib_sum + matrix[coord_y_local][coord_x]
                coord_x += 1
            time.sleep(0.5)
            print('Фиббоначи = ', fib_sum)

        for coord_y in matrix.keys():  # Запускаем проверки для каждой строки
            print('2^', coord_y, ' = ', matrix[coord_y][1:-1], end=' : ') # Срезаем лишние нули в строках
            check_sum(matrix[coord_y])
            check_triangle(coord_y, matrix)
            check_fib(coord_y, matrix)

    old_string = []
    new_string = []
    matrix = {}
    for coord_x in range(0, quanity_lines + 2, 1):  # формируем первую строку вручную
        if coord_x == 1:
            old_string.append(1)
        else:
            old_string.append(0)
    matrix[0] = old_string  # Запись нулевого элемента в матрицу
    for coord_y in range(1, quanity_lines, 1):
        new_string = [0]
        for coord_x in range(1, quanity_lines + 2, 1):
            new_string.append(old_string[coord_x - 1] + old_string[coord_x])
        old_string = new_string  # Формируемая строка становиться существующей
        matrix[coord_y] = old_string
    global_check(matrix)


def sequances(quanity_lines):
    print('\nПоследовательности для проверки:')

    # Формирование списка со степенями двойки
    grades_of_two = []
    for grade in range(0, quanity_lines):
        grades_of_two.append(2 ** grade)
    print('1.Степени двойки    =', grades_of_two)

    # Формирование ряда фибоначи
    fib_seq = [0, 1, ]
    fib_summ = 0
    coord_x = 1
    while True:
        fib_seq.append(fib_seq[len(fib_seq) - 1] + fib_seq[len(fib_seq) - 2])
        if len(fib_seq) > quanity_lines:
            print('2.Ряд фиббоначи     =', fib_seq)
            break

    # Формирование ряда треугольных чисел
    tri_nums_list = [0, ]
    for coord_y in range(0, quanity_lines - 1, 1):
        tri_number = int(0.5 * coord_y * (coord_y + 1))
        tri_nums_list.append(tri_number)
    print('3.Треугольные числа =', tri_nums_list)


paskal_triangle(10)  # quanity_lines -- количество строчек
sequances(10)  # Печать последовательность самих по себе, вне парадигмы матрицы
