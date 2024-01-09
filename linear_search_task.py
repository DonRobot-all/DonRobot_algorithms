def linear_search():
    sentense = input().split()
    min_characters = len(sentense[0])
    min_word = ''
    for word in sentense:
        lenght = len(word)
        if lenght < min_characters:
            min_characters = lenght
            min_word = word
        elif lenght == min_characters:
            min_word += ' ' + word
    return min_word


if __name__ == '__main__':
    print(linear_search())
