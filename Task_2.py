'''Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. '''

from random import randint
numbers = []
for i in range(13):
    numbers.append(randint(1, 8))

new_list = []
for elements in set(numbers):
    if numbers.count(elements) > 1:
        new_list.append(elements)


print(f'{numbers}')
print(f'{new_list}')