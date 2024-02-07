from chapter_11.word import Word
word = Word('hello', 'xin chao')
word1 = Word('hello', 'xin chao')
word2 = Word('hello', 'xin chao')
word3 = Word('hello', 'xin chao')
words = [word, word1, word2, word3]
print(word == word2)

dictionary = {}

for item in words:
    print(item)
    dictionary.setdefault(item, 0)
    dictionary[item] += 1

print(dictionary.items())