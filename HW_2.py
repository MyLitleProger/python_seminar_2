# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

sum_number = int(input('Введите первое число: '))
product_number = int(input('Введите второе число: '))

number_1 = 1
number_2 = 1
# за предел циклов была взята сумма задуманных чисел, так как дальше нет смысла искать,
# а в случает если одно из чисел будет = 1, то произведение уже не будет находиться
# первый цикл будет искать первое значение
while number_1 < sum_number:
    # второй цикл будет искать второе число сравнивая его с первым числом
    while number_2 < sum_number:
        if sum_number == number_1 + number_2 and product_number == number_1 * number_2:
            print('while')
            print(f'{sum_number} = {number_1} + {number_2}')
            print(f'{product_number} = {number_1} * {number_2}')
            print(f'{sum_number} {product_number} -> {number_1} {number_2}')
            # оператора break вернет в верхний цикл
            break
        number_2 += 1
    if sum_number == number_1 + number_2 and product_number == number_1 * number_2:
        break
    # по завершению второе число сбрасывается и сравнивается со следующим первым числом
    number_2 = 1
    number_1 += 1
else:
    print('ниодно из чисел не подошло!')

# через цикл for

number_1 = 1
number_2 = 1

for number_1 in range(1, sum_number):
    for number_2 in range(1, sum_number):
        if sum_number == number_1 + number_2 and product_number == number_1 * number_2:
            print('for')
            print(f'{sum_number} = {number_1} + {number_2}')
            print(f'{product_number} = {number_1} * {number_2}')
            print(f'{sum_number} {product_number} -> {number_1} {number_2}')
            break
    if sum_number == number_1 + number_2 and product_number == number_1 * number_2:
        break
else:
    print('ниодно из чисел не подошло!')
