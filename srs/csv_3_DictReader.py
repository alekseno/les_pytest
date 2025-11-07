import csv

with open('srs/people_3.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)  # ← передаём только открытый файл
    for row in reader:
        print(row)

#Если вам нужно вывести заголовки, доступ к ним можно получить, обратившись к свойству .fieldnames у объекта итератора:

"""
#задаем заголовки вручную, если их нет

import csv

with open('people.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=['Имя', 'Возраст', 'Город'])
    print("Заголовки:", reader.fieldnames)
    for row in reader:
        print(row)"""

#=====================================================
"""Чтобы Python не терял “лишние” значения, у класса csv.DictReader есть специальный параметр — restkey. Он указывает ключ, под которым будут собраны все “лишние” значения (в виде списка).

import csv

with open('people.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=['Имя', 'Возраст'], restkey='Остальные данные')
    for row in reader:
        print(row)

"""

#==============================================
"""
если данных в строке наоборот не хватает restval

import csv

with open('people.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=['Имя', 'Возраст', 'Город', 'email'], restval='_')
    for row in reader:
        print(row)

"""
#=====================================================
"""
Уже знакомый вам параметр delimiter, который отвечает за символ-разделитель — знак,  чем разделяются значения в строке.

reader = csv.DictReader(f, delimiter=';')
"""