alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

output = []


def inputs():
    d = input("Cypher: ")
    run(1, d)


def run(off, b):
    for y in range(27):
        for x in b:
            if str(x).isalpha():
                index = alphabet.index(x)
                output.append(alphabet[index - off])
            elif str(x) == " ":
                output.append(" ")
            else:
                print("Please only use letters")
                output.clear()
                inputs()
        else:
            print(str(off) + ": " + str("".join(output)))
            output.clear()
            off += 1
            if off == 27:
                print("")
                inputs()


inputs()