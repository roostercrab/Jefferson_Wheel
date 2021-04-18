import string
from keys import wheels


def listify(word):
    return [char for char in word]

# Need to divide list into 26 character chunks, and pad them out to 26 characters


def encode_message(message):
    whitespaced = "".join(message.split())
    upcased = whitespaced.upper()
    listified = listify(upcased)
    encoded_list = []
    wheel = 0
    for char in listified:
        position = string.ascii_uppercase.index(char)
        encoded_list.append(wheels[wheel][position])
        wheel += 1
    encoded_string = ''.join([elem for elem in encoded_list])
    print(encoded_string)


message = input("Need input: ")
encode_message(message)
