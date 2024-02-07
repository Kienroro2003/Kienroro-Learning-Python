import webbrowser

import requests, bs4, scrapping_traslate

link_web = []
words = []
first = True

url = 'https://dictionary.cambridge.org/dictionary/english/cohesive'

res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())
while len(words) != 20:
    pronounClassName = '.'.join('ipa dipa lpr-2 lpl-1'.split(' '))
    wordClassName = '.'.join('hw dhw'.split(' '))
    typeWordClassName = '.'.join('pos dpos'.split(' '))
    linkClassName = '.'.join('hul-u hul-u0 hax lmb-10 lcs'.split(' ')) + ' a'
    pronoun = soup.select(f'.{pronounClassName}')[1].getText()
    word = soup.select(f'.{wordClassName}')[0].getText()
    typeWord = soup.select(f'.{typeWordClassName}')[0].getText()
    links = soup.select(f'.{linkClassName}')
    for element in links:
        link_web.append(element.get('href'))
    meaningVietnames = scrapping_traslate.translate_word(word)
    newWord = f'new Word(\"{word}\", \"{meaningVietnames}\", \"{pronoun}\", Type.{typeWord.upper()}) '
    if first:
        newWord = 'Word word = ' + newWord
        first = False
    else:
        newWord = 'word = ' + newWord
    print(newWord + ';\ndictionary.add(word);')

    url = link_web.pop(0)
    if ' https://dictionary.cambridge.org/dictionary/english/affix-to?topic=connecting-and-combining ' == url:
        url = link_web.pop(0)
    res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
