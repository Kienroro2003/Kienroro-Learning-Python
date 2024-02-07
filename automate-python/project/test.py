from chapter_11.word import Word


dictionary = {}
dictionary.setdefault(Word('hello', 'xin chao'), 0)
dictionary.setdefault(Word('bye', 'tam biet'), 0)
dictionary.setdefault(Word('go', 'di'), 0)
dictionary.setdefault(Word('leave', 'roi di'), 0)

word = Word('hello', '')
print(word in dictionary)