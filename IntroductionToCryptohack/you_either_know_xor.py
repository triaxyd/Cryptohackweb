import base64

ciphertext = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key = "crypto"

bytes_cipher = bytes.fromhex(ciphertext).decode()



byte_key = bytearray()
byte_key.extend(map(ord,key))
print(byte_key)

