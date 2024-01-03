from Crypto.PublicKey import RSA

# first convert .der file to .pem with 
# openssl x509 -inform der -in CERTIFICATE.der -out CERTIFICATE.pem

file_path = '/Users/triantafyllosxydis/Programming/Cryptohackweb/GENERAL/DATA_FORMATS/CERTainly_not/CERTIFICATE.pem'
f = open(file_path,'r')
key = RSA.import_key(f.read())

print(key.n)
f.close()