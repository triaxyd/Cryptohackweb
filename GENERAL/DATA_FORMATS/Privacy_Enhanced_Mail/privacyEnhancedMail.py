from Crypto.PublicKey import RSA

file_path = '/Users/triantafyllosxydis/Programming/Cryptohackweb/GENERAL/DATA_FORMATS/Privacy-EnhancedMail/pem1.pem'
f = open(file_path,'r')
key = RSA.import_key(f.read())

print(key.d)
f.close()

