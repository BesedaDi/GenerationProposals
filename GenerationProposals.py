###
###
""" Case-study #6 Генерация предложения
Разработчики:
Беседина Д.В., Сецков М.

"""
import random
def word():
    f = open('input.txt', 'r', encoding='utf8')
    text = f.read()
    text = text.replace('\n', ' ')
    import re
    text = re.sub('[@#$%^&*:]', '', text)
    res = re.sub(r' ,', ', ', text)
    res = res.replace(' .', '.')
    res = res.replace(' ;', ';')
    res = res.replace(' !', '!')
    res = res.replace(' ?', '?')

    text1 = text = re.sub('[,.!?;]', '', text)
    word = list(text1.split())
    print(word)
word()


