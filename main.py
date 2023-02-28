morse_code = {'a': ".- ", 'b': '-... ', 'c': "-.-. ", 'd': "-.. ", 'e': ". ", 'f': '..-. ', 'g': '--. ', 'h': '.... ',
              'i': '.. ', 'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ', 'p': '.--. ',
              'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ',
              'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ',
              '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ', '.': '.-.-.- ',
              ',': '--..-- ', '?': '..--.. ', "'": '.----. ', '!': '-.-.-- '}


def translate(word):
    translation = ''
    for letter in word:
        if letter == ' ':
            translation += '/ '
        else:
            translation += morse_code[letter]
    print(translation)


translating = True
print("Welcome to the Morse Code Translator™")

while translating:
    sentence = input("Please enter the word or sentence you'd like to translate: ").lower()

    translate(sentence)

    translate_again = input('Would you like to translate another word or sentence? y/n ').lower()

    if translate_again == 'n':
        translating = False
        print("Thank you for using our service.")
