
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    flat_list=[]
    for row in matrix:
        flat_list.extend(row)
    for i in flat_list:
        return "".join(chr(i) for i in flat_list)
    

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(bytes2matrix(matrix))
print(matrix2bytes(matrix))
