import string

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

def encode_message(message):
    whitespaced = "".join(message.split())
    upcased = whitespaced.upper()
    listified = listify(upcased)
    encoded_list = []
    wheel = 0
    for char in listified:
      position = string.ascii_uppercase.index(char)
      print(wheel)
      encoded_list.append(wheels[wheel][position])
      wheel += 1
    encoded_string = ''.join([elem for elem in encoded_list])
    print(encoded_string)

message = input("Need input: ")
encode_message(message)

