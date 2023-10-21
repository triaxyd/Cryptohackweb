import base64

message = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
message = bytes.fromhex(message) #turn hex to bytes
message = base64.b64encode(message) #encode base64 to byte object
message = message.decode() #turn byte to string
print(message)