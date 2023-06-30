'''
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга?
Какие вещи уникальны, есть только у одного друга?
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует.
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
'''

dict_frends_atribute = {"Сергей": ("топор", "палатка", "мыло"),\
                        "Петр": ("компас", "полотенце", "кружка"),\
                        "Иван": ("котелок", "нож", "зажигалка")
                        }

# Какие вещи взяли все три друга
def list_atribute_frends(dict_list):
    list_atribute = []
    for atribut in dict_list.values():
        list_atribute += atribut
    return list_atribute

count = 0

def dict_unicum_atribute (dict_list):
    name_not_atribute = []
    new_dict = {}
    count = 0
    for key, value in dict_frends_atribute.items():
        name_not_atribute.append(key)
        new_dict[key] = []
        for j in value:
            for k in list_atribute_frends(dict_frends_atribute):
                if k == j:
                    count += 1
            if count == 1:
                new_dict[key] += [j]
            if count > 1:
                name_not_atribute.remove(key)
            count = 0
    print(f'В этом списке людей отсутствует вещь, которая дублируется у остальных: {name_not_atribute}\n')
    return new_dict


print(f"Вещи, которые взяли три друга: {list_atribute_frends(dict_frends_atribute)}\n")
print(f"Уникальные вещи, которые взял каждый друг: {dict_unicum_atribute(dict_frends_atribute)}\n")