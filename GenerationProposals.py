###
###
""" Case-study #6 Генерация предложения
Разработчики:
Беседина Д.В., Сецков М.

"""
import random

name = input('Введите имя файла, который хранит исходный текст:')


def word(name, rez='ERROR'):
    while rez == 'ERROR':
        try:
            file = open(name, 'r', encoding='utf8')
            text = file.read()
            rez = 'OK'
        except IOError as e:
            print(u'Такого файла не существует. Повторите попытку.')
            rez = 'ERROR'
            name = input('Введите имя файла, который хранит исходный текст:')
    import re
    text = text.replace('\n', ' ')
    text = re.sub('[@#$%^&*:]', '', text)
    res = re.sub(r' ,', ', ', text)
    res = res.replace(' .', '.')
    res = res.replace(' ;', ';')
    res = res.replace(' !', '!')
    res = res.replace(' ?', '?')

    text1 = text = re.sub('[,.!?;]', '', text)
    word = list(text1.split())
    print(word)
word(name, rez='ERROR')
