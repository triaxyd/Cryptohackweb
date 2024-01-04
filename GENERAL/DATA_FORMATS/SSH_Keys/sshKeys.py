
from Crypto.PublicKey import RSA

file_path = '/Users/triantafyllosxydis/Programming/Cryptohackweb/GENERAL/DATA_FORMATS/SSH_Keys/bruceRSA1.pub'
f = open(file_path,'r')
key = RSA.import_key(f.read())
print(key.n)
f.close()