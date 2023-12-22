stringtext = "label"

new_string = ""
for c in stringtext:
    temp = ord(c)
    xor_temp = temp ^ 13
    new_char = chr(xor_temp)
    new_string += new_char
print(new_string)