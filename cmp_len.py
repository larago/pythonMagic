#encoding=utf8

class Word(str):
    '''store sort of word, define several ways to compare them'''

    def __new__(cls, word):
        if ' ' in word:
            print 'Value contains spaces. Truncating to first space.'
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

print Word('amazing') == Word('amazing')