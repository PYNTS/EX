def break_words(stuff):
    """Ta funkcja rozbija zdanie na slowa."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sortuje slowa."""
    return sorted(words)

def print_first_word(words):
    """Drukuje pierwsze slowo i usuwa je ze zdania."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Drukuje ostatnie slowo i usuwa je ze zdania."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Pobiera pelne zdanie i zwraca posortowane slowa."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Drukuje pierwsze i ostatnie slowo zdania."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sortuje slowa, a nastepnie drukuje pierwsze i ostatnie."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
