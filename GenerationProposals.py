###
###
""" Case-study #6 Генерация предложения
Разработчики:
Беседина Д.В., Сицков М.

"""
import random

symbols = ['!','@','#','$','%']
f = open('input.txt','r', encoding='utf8')
text = f.read()
for symbol in symbols:
    if symbol in text:
        text = text.replace(symbol,'')
import string
import re


pat = "\text+([{}]+)".format(re.escape(string.punctuation))
res = re.sub("\s{2,}", " ", re.sub(pat, r"\1", text))
text = res.replace('\n', ' ')
print(text)
