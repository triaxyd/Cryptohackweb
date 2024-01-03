from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

received = json_recv()

def decode_things(encoded_string,encoded_type):
    if encoded_type == "base64":
            decoded = base64.b64decode(encoded_string).decode('utf-8') # wow so encode
    elif encoded_type == "hex":
        decoded = bytes.fromhex(encoded_string).decode('utf-8')
    elif encoded_type == "rot13":
        decoded= bytes(codecs.decode(encoded_string,'rot13')).decode()
    elif encoded_type == "bigint":
        decoded = bytes(long_to_bytes(int(encoded_string),16)).decode()
    elif encoded_type == "utf-8":
        decoded = ''.join(chr(c) for c in encoded_string)


for i in range (100):
    received = json_recv()
    print('Type of received message:',received["type"])
    encoded_type = received['type']
    print("Received encoded value: ",received["encoded"])
    encoded_string = received["encoded"]

    to_send = {
        "decoded": decode_things(encoded_string,encoded_type)
    }
    json_send(to_send)
print(json_recv())
