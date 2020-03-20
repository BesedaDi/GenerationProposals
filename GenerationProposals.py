###
###
""" Case-study #6 Генерация предложения
Разработчики:
Беседина Д.В.(40%), Сецков М.(70%)

"""
import random
import re


def word():
    name = input('Введите имя файла, который хранит исходный текст:')
    rez = 'ERROR'
    while rez == 'ERROR':
        try:
            file = open(name, 'r', encoding='utf8')
            text = file.read()
            rez = 'OK'
        except IOError as e:
            print(u'Такого файла не существует. Повторите попытку.')
            rez = 'ERROR'
            name = input('Введите имя файла, который хранит исходный текст:')
    text = text.replace('\n', ' ')
    text = re.sub('[@#$%^&*:]', '', text)
    res = re.sub(r' ,', ', ', text)
    res = res.replace(' .', '.')
    res = res.replace(' ;', ';')
    res = res.replace(' !', '!')
    res = res.replace(' ?', '?')

    text1 = text = re.sub('[,.!?;]', '', text)
    word = list(text1.split())
    return word


source_words = word()
list_start = []
for word in source_words:
    if word.istitle():
        list_start.append(word)
for i in list_start:
    if i[-1] == '.':
        list_start.remove(i)

listLinks = []
for word in source_words:
    index = source_words.index(word)
    listLinks.append(word)
    listMore = []
    if index != len(source_words) - 1:
        listMore.append(source_words[index + 1])
    wordAmount = source_words.count(word)
    if wordAmount > 1:
        start = index + 1
        end = len(source_words)
        for i in range(wordAmount - 1):
            index = source_words.index(word, start, end)
            listMore.append(source_words[index + 1])
            if source_words[index] != source_words[-1]:
                start = index + 1
            else:
                break
    listLinks.append(listMore)
listLinks = listLinks[:-2]

n = int(input('Сколько предложений нужно сгенерировать из исходного текста? '))
amount_startWords = len(list_start)
for i in range(n):
    firstWord = random.randint(0, amount_startWords - 1)
    first_word = list_start[firstWord]
    sent = first_word + ' '
    indexFirst = listLinks.index(first_word)
    for i in range(random.randint(5, 20)):
        if len(listLinks[indexFirst + 1]) > 1:
            lenght = len(listLinks[indexFirst + 1])
            number = random.randint(0, lenght)
            secWord = (listLinks[indexFirst + 1])[number - 1]
            sent += str(secWord) + ' '
            if (str(secWord))[-1] == '.':
                break
            indexFirst = listLinks.index(str(secWord))
        else:
            secWord = listLinks[indexFirst + 1]
            sent += (str(secWord))[2:-2] + ' '
            if ((str(secWord))[2:-2])[-1] == '.':
                break
            indexFirst = listLinks.index((str(secWord))[2:-2])
    if sent[-2] != '.':
        print(sent[:-1], end='')
        print('.', end=' ')
    else:
        print(sent, end='')
