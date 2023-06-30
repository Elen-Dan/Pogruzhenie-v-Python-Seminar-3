'''В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

import re
import pprint

some_text = 'Почему применение сотрудниками нейросетей все чаще приводит к судебным искам против работодателей? \
    Как понять, не выдает ли подчиненный за свою работу «помощь» нейросети? \
    Компании начинают массово использовать нейросети в работе — для написания текстов, составления рекламных объявлений, \
    поиска информации и общения с клиентами по скриптам. «Согласно данным Tele2, только в России количество пользователей ChatGPT и Midjourney \
    всего за два первых месяца этого года увеличилось в пять раз. Нет никаких сомнений, что большинство из них начнут использовать нейросети в работе»,\
    — констатирует Глеб Антипов, исполнительный директор технологической компании «ДиСи Инжиниринг». Многие компании это приветствуют \
    или хотя бы не против, ведь нейросети помогают снизить издержки.'


my_dict = dict()
words = re.sub(r'\W', ' ', some_text).lower().split()

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1


pprint.pprint(my_dict)