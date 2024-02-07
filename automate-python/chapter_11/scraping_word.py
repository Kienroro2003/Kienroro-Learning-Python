import csv
import os.path
import pprint

import requests, bs4, scrapping_traslate

from chapter_11.word import Word


def writeCSV(dictionary):
    file = csv.writer(open(os.path.abspath('./data.csv'), 'w'))
    file.writerows(dictionary)

def readCSV(dictionary):
    file = csv.reader(open(os.path.abspath('./data.csv'), 'r'))
    for row in file:
        word = Word(*row)
        dictionary.append(word)


def textHtml(className, soup, index):
    array = [className, 'headword.tw-bw.dhw.dpos-h_hw b']

    for name in array:
        elements = soup.select(f'.{name}')
        if len(elements) == 0:
            continue
        if len(elements) == 1 and index != 0:
            index = 0
        if len(elements) >= 2 and len(elements) % 2 == 0:
            index = int(len(elements) / 2)
        return elements[index].getText().lower()
    return ''


def translateWord(text):
    url = 'https://dictionary.cambridge.org/dictionary/english/' + text
    res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    pronounClassName = 'page>.pr.dictionary:first-child .ipa.dipa.lpr-2.lpl-1'
    wordClassName = '.'.join('hw dhw'.split(' '))
    typeWordClassName = '.'.join('pos dpos'.split(' '))
    word = textHtml(wordClassName, soup, 0)

    pronoun = textHtml(pronounClassName, soup, 1)
    typeWord = textHtml(typeWordClassName, soup, 0)
    try:
        meaningVietnames = scrapping_traslate.translate_word(word).lower()
    except TypeError:
        return None
    # newWord = f'new Word(\"{word}\", \"{meaningVietnames}\", \"{pronoun}\", Type.{typeWord.upper()}) '
    newWord = Word(word, meaningVietnames, pronoun, typeWord, 1, True)
    return newWord

newword = translateWord('settings')
print(newword)

# def add(word, dictionary):
#     newWord = Word(word, '', '', '', 0, True)
#     if newWord in dictionary and dictionary[dictionary.index(newWord)].isUsed:
#         dictionary[dictionary.index(newWord)].increaseCount()
#         return None
#     else:
#         newWord = translateWord(word)
#         if newWord is None:
#             return None
#         if newWord in dictionary and dictionary[dictionary.index(newWord)].isUsed:
#             dictionary[dictionary.index(newWord)].increaseCount()
#         elif newWord in dictionary and not dictionary[dictionary.index(newWord)].isUsed:
#             return None
#         else:
#             return newWord
#
#
# text = '''Create one runner class named as ‘BookTestRunner.java’ just to test the application once. It implements ‘CommandLineRunner.java’. In this example we are saving 4 books in MongoDB. In addition, updating ID of last book manually(which is allowed) and the name of the author. MongoDB will consider this as a new record. At the last, retrieve all the saved books and display it in the console. For example, below is the code.'''
#
#
# text = ' '.join(text.split('\n')).translate({ord(i): None for i in '.(),?!:+-*/@#$%^&<>'}).lower().split(' ')
#
# dictionary = []
# readCSV(dictionary)
# for word in text:
#     newWord = add(word, dictionary)
#     if newWord is not None:
#         dictionary.append(newWord)
#
#
# writeCSV(dictionary)
