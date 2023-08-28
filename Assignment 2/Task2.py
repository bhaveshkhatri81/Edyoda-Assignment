
ascii_dict = {}


for letter in range(ord('a'), ord('z') + 1):

    ascii_dict[chr(letter)] = letter


print(ascii_dict)
