import base64

def xor_them(xs,ys):
    return bytes(x ^ y for x,y in zip(xs,ys))

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_key2= "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_with_keys = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


bytes_key1 = bytes.fromhex(key1)
bytes_key1_key2 = bytes.fromhex(key1_key2)
bytes_key2_key3 = bytes.fromhex(key2_key3)
bytes_flag_with_keys = bytes.fromhex(flag_with_keys)


bytes_key2 = xor_them(bytes_key1,bytes_key1_key2)
bytes_key3 = xor_them(bytes_key2,bytes_key2_key3)

#xor of 3 keys
bytes_temp = xor_them(bytes_key1,bytes_key2)
bytes_temp = xor_them(bytes_temp,bytes_key3) 

bytes_flag = xor_them(bytes_temp,bytes_flag_with_keys)

flag = bytes_flag.decode()

print(flag)

if (xor_them(bytes_key1,bytes_key2) == bytes_key1_key2):
    print("Found correct key2")

if (xor_them(bytes_key2,bytes_key3) == bytes_key2_key3):
    print("Found correct key3")

t1 = xor_them(bytes_flag,bytes_key1)
t2 = xor_them(t1,bytes_key2)
t3 = xor_them(t2,bytes_key3)

if t3 == bytes_flag_with_keys:
    print("Found correct flag")



