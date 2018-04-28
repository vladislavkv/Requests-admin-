import requests

key = 'trnsl.1.1.20180428T041521Z.072966e4a243b04b.40f01b187f24cfe83251005676e3620fc70c3b2d'

def repeat():
    lng = ''

    print('С какого языка перевести?\n'
          '1: С английского\n'
          '2: С русского\n'
          '3: С польского\n')

    num1 = int(input())
    print()

    if num1 == 1:
        lng1 = 'en'
    elif num1 == 2:
        lng1 = 'ru'
    elif num1 == 3:
        lng1 = 'pl'

    print('На какой язык перевести?\n'
          '1: На английский\n'
          '2: На русский\n'
          '3: На польский\n')

    num2 = int(input())
    print()

    if num2 == 1:
        lng2 = '-en'
    elif num2 == 2:
        lng2 = '-ru'
    elif num2 == 3:
        lng2 = '-pl'

    lng = lng1 + lng2

    data = {'key' : key,
            'text' : input('Введите текст: '),
            'lang' : lng,
            'format' : 'plain'}

    request = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data)

    dict_request = request.json()

    print()
    print(dict_request['text'])
    print()

    repeat()
    
repeat()
