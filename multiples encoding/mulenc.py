import string

# morse_sample = './-./-.-./.-./../-./---/../-..'
def morse_decrypter(sample):
    #define morse dict :
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
    REV_MORSE_DICT = {}
    for key, value in MORSE_CODE_DICT.items():
        REV_MORSE_DICT[value] = key
    # print(REV_MORSE_DICT)
    morse = sample.split('/')
    # print(morse)
    ls = []
    for item in morse :
        ls.append(REV_MORSE_DICT[item])
    # print(ls)
    answer = ''.join(ls)
    print(answer)
    return answer
# morse_decrypter(morse_sample)
