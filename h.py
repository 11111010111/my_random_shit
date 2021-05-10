c = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
output = []


def inputs():
    b = input("Cypher: ")
    run(c, b)


def run(c, b):
    offset = c
    for x in b:
        if str(x).isalpha():
            pass
        else:
            print("Please only use letters")
            output.clear()
            inputs()
        index = alphabet.index(x)
        output.append(alphabet[index - offset])
    else:
        print(str(c) + ": " + str("".join(output)))
        output.clear()
        c += 1
        if c == 27:
            print("")
            inputs()
        run(c, b)

inputs()
