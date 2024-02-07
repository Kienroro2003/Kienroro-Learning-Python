word = Word('hello', 'xin chao')
word1 = Word('hello', 'xin chao')
word2 = Word('hello', 'xin chao')
word3 = Word('hello', 'xin chao')
words = [word, word1, word2, word3]

dictionary = {}
dictionary.setdefault(word, 1)

for item in words:
    dictionary.setdefault(item, 1)
    dictionary[item] += 1

print(dictionary)