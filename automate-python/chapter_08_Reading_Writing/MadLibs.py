import re

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
sentenceRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
find = sentenceRegex.findall(text)

for word in find:
    print(f"Enter an {word.lower()}:")
    text = text.replace(word, input(), 1)
    print(text)