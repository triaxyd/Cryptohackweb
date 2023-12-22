
message = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_message = bytes.fromhex(message).decode()
print(bytes_message)

for key in range(0,256):
    possible_solution = ""
    for k in bytes_message:
        new_char = chr(ord(k) ^ key)
        possible_solution += new_char
    if "crypto" in possible_solution:
        print (possible_solution)