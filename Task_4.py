'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.
'''

stuff = {'палатка': 300, 'спальный мешок': 150, 'консервы': 100, 'нож': 50,
          'термос': 200, 'аптечка': 150, 'термобелье': 50, 'бинокль': 150, 'зажигалка': 50,
          'батарейки': 200, 'носки': 100, 'мыльница': 100, 'фонарь': 100, 'бинт': 200}

weight_limit = 200
temp_keys = []
temp_values = []
result = []
goods_keys = list(stuff.keys())
goods_values = list(stuff.values())

print(goods_keys)
print(goods_values)

for i in range(len(goods_keys)):
    if goods_values[i] <= weight_limit:
        temp_keys = []
        temp_values = []
        for j in range(i, len(goods_keys)):
            if sum(temp_values) + goods_values[j] <= weight_limit:
                temp_values.append(goods_values[j])
                temp_keys.append(goods_keys[j])
                print(temp_keys)