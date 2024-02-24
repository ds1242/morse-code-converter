MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def convert_to_morse(letter):
    morse_output = MORSE_CODE_DICT.get(letter.upper())
    return morse_output

def split_words_letters(array):
    output = []
    for i in array:
        word_arr = list(i)
        converted_letters = []
        for j in word_arr:
            converted_letters.append(convert_to_morse(j))
        output.append(" ".join(converted_letters))
    return output

user_input  = input("Please enter a value to be converted to Morse Code: \n").split()

converted_string = "/".join(split_words_letters(user_input))
print(converted_string)
