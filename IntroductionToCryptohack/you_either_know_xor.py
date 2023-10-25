import base64

ciphertext = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytes_cipher = bytes.fromhex(ciphertext)

#we know that the flag has the format crypto{ so we xor the first 7 chars of the message with it

# the partial key is "myXORke" so the key is myXORkey probably
partial_key = "".join(chr(c ^ ord(f)) for c, f in zip(bytes_cipher[:7], "crypto{")) + "y"

#the key has the same length as ciphertext
complete_key = (partial_key * (len(ciphertext)//len(partial_key)+1))[:len(ciphertext)]


flag = "".join(chr(c ^ ord(f)) for c, f in zip(bytes_cipher, complete_key))

print(flag)

