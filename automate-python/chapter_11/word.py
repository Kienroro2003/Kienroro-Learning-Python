
class Word:
    word, meaning, pronoun, type, count, isUsed = '', '', '', '', 0, True

    def __init__(self, word, meaning, pronoun, type, count, isUsed) -> None:
        self.word = word
        self.meaning = meaning
        self.pronoun = pronoun
        self.type = type
        self.count = int(count)
        self.isUsed = bool(isUsed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Word):
            return NotImplemented
        return self.word == o.word

    def __hash__(self):
        return hash(self.word)

    def __str__(self) -> str:
        # return f'\"english word\": \"{self.word}\", \"meaning\": \"{self.meaning}\", \"type word\": \"{self.type}\", \"pronoun\": \"{self.pronoun}\",'
        return str([self.word, self.meaning, self.pronoun, self.type, self.count, self.isUsed])

    def __iter__(self):
        return iter([self.word, self.meaning, self.pronoun, self.type, self.count, self.isUsed])

    def increaseCount(self):
        self.count += 1
