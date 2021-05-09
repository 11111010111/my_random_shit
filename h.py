string = input("Cypher: ")
c = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
output = []
a = string.split(" ")
b = list("".join(a))


def run(c1):
    offset = c1
    for x in b:
        index = alphabet.index(x)
        output.append(alphabet[index - offset])
    else:
        print(str(c1) + ": " + str("".join(output)))
        output.clear()
        c1 += 1
        if c1 == 27:
            quit()
        run(c1)


run(c)
