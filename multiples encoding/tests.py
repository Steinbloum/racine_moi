import base64
import codecs
import binascii
enigma = 'cW-QFX>(`'
enigma.strip("'")
print(enigma)
enigma = base64.b85decode(enigma)
enigma = enigma.decode('ascii')
print(type(enigma))
# print(enigma)
# enigma = binascii.hexlify(enigma)
# print(enigma)
# enigma = bytes.fromhex(enigma)
# enigma = enigma.decode('ascii')
# print(enigma)
# # print(decode)


print(enigma)
