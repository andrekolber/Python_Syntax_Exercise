# def print_upper_words(words):
#     '''takes a list of words and uppercases each word and prints each word on a seperate line'''
#     for word in range(len(words)):
#         words[word] = words[word].upper()
#         print(words[word])
    

# print_upper_words(['hello', 'goodbye', 'sayonara'])

def print_upper_words_e(words, letter1, letter2):
    '''takes a list of words and only prints the words that start with the letter 'e'.'''
    for word in words:
        if word[0] == letter1 or word[0] == letter2:
            print(word)
    

print_upper_words_e(["hello", "hey", "goodbye", "yo", "yes"], 'h', 'y')