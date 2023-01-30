# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка
# содержит N чисел, записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза. Все числа натуральные
# и не превышают 30000.
from random import randint as RI

count_watermelon = int(input('введите количество арбузов: '))

max_weight = 0          # идем от меньшего к большему
min_weight = 30000      # идем от большего к меньшему

for _ in range(1,count_watermelon + 1):
    weight_watermelon = RI(1,30000)
    print(f'вес арбуза {weight_watermelon}')
    # максимальное значение
    if max_weight < weight_watermelon:
        max_weight = weight_watermelon
    # минимальное значение
    if min_weight > weight_watermelon:
        min_weight = weight_watermelon

print(f'макс {max_weight}')
print(f'мин  {min_weight}')