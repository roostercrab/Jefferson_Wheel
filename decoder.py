import string
from keys import wheels

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)


def listify(word):
    return [char for char in word]


def decode_message(message):
    listified = listify(message)
    decoded_list = []
    wheel = 0
    for char in listified:
        position = wheels[wheel].index(char)
        translated = alphabet_list[position]
        decoded_list.append(translated)
        wheel += 1
    decoded_string = ''.join([elem for elem in decoded_list])
    print(decoded_string)


message = input("Need input: ")
decode_message(message.upper())
