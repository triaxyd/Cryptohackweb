from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

byte_string = long_to_bytes(integer)

final = byte_string.decode()

print(final)
