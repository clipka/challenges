from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open("dictionary.txt") as d:
        words = d.readlines()
        words = [w.strip() for w in words]

        return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for s in word:
        s = s.upper()
        if s.isalpha():
            word_value = word_value + int(LETTER_SCORES.get(s))

    return word_value


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value_word = ""
    max_value = 0

    if words == None:
        words = load_words()

    for word in words:
        val = calc_word_value(word)
        if val > max_value:
            max_value = val
            max_value_word = word

    return max_value_word


if __name__ == "__main__":
    pass  # run unittests to validate
