# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.


number = int(input('Введите целое число: '))

fibonachi_0 = 0
fibonachi_1 = 1
i = 3
fibonachi_n = 0
while number > fibonachi_n:
    fibonachi_n = fibonachi_1 + fibonachi_0
    fibonachi_0 = fibonachi_1
    fibonachi_1 = fibonachi_n
    if number == fibonachi_n:
        print(f'Число А является числом фибоначчи по счету {i}')
        break
    i += 1
else:
    print(-1)