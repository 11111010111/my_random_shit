offset = 1
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
    for x in b:
        if str(x).isalpha():
            index = alphabet.index(x)
            output.append(alphabet[index - off])
        elif not str(x).isalpha():
            if str(x) == " ":
                output.append(" ")
            else:
                output.append(str(x))
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
        run(off, b)


inputs()
