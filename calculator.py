import numpy as np

while True:
    first = input("what is the first number???? ")
    if first == "end":
        print("i see you are done")
        print("imma go now ig")
        print("cya")
        quit()
    operation = input("what is the operation i shall do? ")
    if operation == "sqrt":
        pass
    else:
        second = int(input("what is the second number???? "))

    if operation == "+":
        result = float(first) + float(second)
    else:
        if operation == "-":
            result = float(first) - float(second)
        else:
            if operation == "*":
                result = float(first) * float(second)
            else:
                if operation == "/":
                    result = float(first) / float(second)
                else:
                    if operation == "**":
                        result = float(first) ** float(second)
                    else:
                        if operation == "sqrt":
                            result = np.sqrt(float(first))
                        else:
                            print("fuck you for thinking that would actually work")
                            result = "try again dumbass"

    print("the answer to your problem is: " + str(result))
