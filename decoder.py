import string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

wheels = [
    "STODKIFQZAGHYVBXERPCMWNLUJ",
    "HWLMSKEOCGDZAVQITJURNYBXPF",
    "ZSXMGENQFDHOBJIUPYCAKVWRTL",
    "ZNJKHIWOPFTGBLXDCURVAESYMQ",
    "XJSBGAOPWCEUMLQRTHDKYNIZFV",
    "EKXOZIUPRLNWACDHJGFVQTBSMY",
    "VOKUSYZIFRGAQDNXTHBJWMCPEL",
    "EWRBVZYKUSAMHCDGIQTNPJLXFO",
    "RYCOIJHQDPWLSBZXTKMEVFGAUN",
    "SBZNJEMROHFUCXPQITGWKALYDV",
    "MLSAVKNCIUWFTEQRGBDJYXOHPZ",
    "DAZPITGMXBSFKNWEJRUQHCLOYV",
    "BRCJASOWLUNMPKFZVTHDEQGIXY",
    "KRZVCUIGSTFADMNJYPLEBOHXWQ",
    "ZCPBYNFGQMWTHAUOIKLXRSEJDV",
    "ODHRWZXNEMQVJFTSKLPGUABIYC",
    "QKMDLUXSWYZHBINTCGOEPFAVRJ",
    "OYMRGPAQZWESTKBLJDNFIXCHVU",
    "UNLVPSCOHZMBYFIJRTKEXQGWDA",
    "GITCNFUHKJBWEYAZVSDROMLXQP",
    "HKEQBTVZRWPIFUSCDNYJXOAGLM",
    "DRSYGFKXPMEZCNBQJOTWLIUVHA",
    "NOQCSZBXIGVMPFWLDJTKHYUREA",
    "RLUJVIOEMYNZHGKPTDSWBXQCAF",
    "FEJNRKMBPVHITDWZUYGLQSCOAX",
    "QZUJCVFKSNARIEHXGLYTWMDPBO"
]

def listify(word):
    return [char for char in word]

def decode_message(message):
    listified = listify(message)
    decoded_list = []
    wheel = 0
    for char in listified:
      position = wheels[wheel].index(char)
      translated = alphabet[position]
      decoded_list.append(translated)
      wheel += 1
    decoded_string = ''.join([elem for elem in decoded_list])
    print(decoded_string)

message = input("Need input: ")
decode_message(message)

