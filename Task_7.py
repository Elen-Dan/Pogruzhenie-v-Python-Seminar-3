'''Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ - символ, а значение — частота встречи символа в строке.
Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
'''

input_txt = input("Введите какой-нибудь текст: ")

# не используем метод count
my_dict = {}
for letter in input_txt:
    if letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1
print(my_dict)

# используем метод count
new_dict = {}
for letter in set(input_txt):
    new_dict[letter] = input_txt.count(letter)
print(new_dict)