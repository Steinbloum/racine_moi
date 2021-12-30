import binascii
from contextlib import ExitStack
import string
import base64
# morse_sample = './-./-.-./.-./../-./---/../-..'

    

class Decypher():
    def __init__(self) -> None:
        pass

    def decode_morse(self, enigma):
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
        morse = enigma.split('/')
        # print(morse)
        ls = []
        for item in morse :
            ls.append(REV_MORSE_DICT[item])
        # print(ls)
        answer = ''.join(ls)
        print(answer)
        return answer.lower()

    def decode_b64(self, enigma):
        try:
            str_bytes = enigma.encode('ascii')
            enigmabytes = base64.b64decode(str_bytes)
            enigma = enigmabytes.decode('ascii')
            return enigma
        except Exception:
            print("not b64")
            
        try:
            str_bytes = enigma.encode('ascii')
            enigmabytes = base64.b32decode(str_bytes)
            enigma = enigmabytes.decode('ascii')
            print('Its b32')
            return enigma
        except Exception:
            print('there is a problem here')

    def decode_b85(self, enigma):
        enigma = base64.b85decode(enigma)
        enigma = enigma.decode('ascii')
        print('DECODED B85')
        return enigma

    def decode_hex(self, enigma):
        enigma = bytes.fromhex(enigma)
        enigma = enigma.decode('ascii')
        return enigma        

    def id_encoding(self, enigma):
        if "/." in enigma:
            print("This seems to be morse")
            return "morse"
        elif len(enigma) % 4 ==0:
            print("could be b64")
            if self.decode_b64(enigma) == None:
                print("it's not b64")
            else :
                return 'b64'
        if all(c in string.hexdigits for c in enigma):
            print("it's hexadecimal")
            return "hex"
        
        else:
            return "b85"


    def format_enigma(self, enigma):
        enigma = enigma.split(' ')[-2]
        # print(enigma)
        enigma = enigma.split('\n')[0]
        # print(enigma)
        enigma = enigma.strip("'")
        return enigma

    def run_decypher(self, sample):
        # sample = sample.strip("'")
        sample = self.format_enigma(sample)
        encoding_format = self.id_encoding(sample)
        if encoding_format == 'morse':
            return self.decode_morse(sample)
        elif encoding_format == "b64":
            return self.decode_b64(sample)
        elif encoding_format == "hex":
            return self.decode_hex(sample)
        elif encoding_format =="b85":
            return self.decode_b85(sample)
    


# sample = './-./-.-./.-./../-./---/../-..'
# sample = '6170707265636961746f7273'
# print(all(c in string.hexdigits for c in sample))



d = Decypher()
# sample = sample.strip("'")
# print(d.run_decypher(sample))

