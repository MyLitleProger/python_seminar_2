# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите целое число: '))
degree_two = 1
degree = 0
while degree_two < number:                      # пока 2 в степени не будет больше числа
    print(f'2^{degree} = {degree_two}')         #
    degree += 1                                 #
    degree_two = 2**degree                      # просчет идет последним что бы степень 2
                                                # не выходила за число при выводе
