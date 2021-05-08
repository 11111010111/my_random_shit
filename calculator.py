# This is the horrid code to my calculator #
# variables (theres not many here lol)
history = []
running = False
operators = ["+", "-", "*", ".", "/", "**", "sqrt", "%", "<", "=", ">", "=/=", "//", "crt"]
starting = True


def end():  # end function ends the program
    print("i see you are done")
    print("imma go now ig")
    print("cya")
    quit()


def check_float(potential_float):  # check if the input is a float
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


def commands(command1):  # looks for commands in inputs
    if command1 == "end":  # looks for the "end" command
        end()
    elif command1 == "commands":  # looks for the "commands" command
        print("The commands are:")  # prints all commands
        print("hist, end, commands, back")
        print("Hist: shows all results")
        print("End: ends program")
        print("Help: shows all commands")
        print("Command: goes back to starting prompt")
    elif command1 == "hist":  # looks for "hist" command
        print(history)  # prints the list of results recorded
    elif command1 == "start":  # start command starts the actual calculator
        print("Lets go!!")
        go()
    elif command1 == "back":  # goes back to starting screen
        helps(False)  # "False" means the welcome text will not show up
    elif command1 == "perfection":  # secret command. SHHHHHHHHHHH
        print("I know right?!")
    elif command1 == "poggers":
        print("poggers")
    else:
        print("Please enter a valid command")  # if command is not recognized an error will appear
        helps(False)  # will go back to starting screen
    if not running:
        helps(False)
    else:
        go()  # if running is true it will restart the calculator


def com(command1):  # for looking for commands in first
    if command1 == "command":
        helps(False)
    elif command1 == "end":
        end()
    elif command1 == "perfection":
        print("I know right?!")
        get_first()
    elif command1 == "poggers":
        print("poggers")
        get_first()
    else:
        print("Not a valid integer/float")
        print("Please try again")
        go()


def helps(starting1):
    if starting1:
        print("WELCOME TO MY CALCULATOR")
    print("Command ('start' to start)")
    command = input("> ")
    commands(command)


def square_root(x):
    x = x ** (1/2)
    return x


def get_first():
    print("First Command / Number")
    first = input("> ")
    if first == "pi":
        first = 3.14159265359
    elif first == "e":
        first = 2.718281828459045
    elif first == "phi":
        first = 1.618033988749895
    elif first == "rt2":
        first = square_root(2)
    elif first == "rt3":
        first = square_root(3)
    if check_float(first):
        pass
    else:
        com(first)
    return first


def get_operator():
    print("Operator")
    operation = input("> ")
    if operation in operators:
        pass
    else:
        print("That is not an operator")
        print("Please try again")
        operation = 0
        get_operator()
    return operation


def single_argument_check(operation):
    if operation == "sqrt":
        second = 0
        pass
    elif operation == "crt":
        second = 0
        pass
    else:
        print("Second Number")
        second = input("> ")
    return second


def the_actual_math(first, operation, second):
    if operation == operators[0]:
        result = float(first) + float(second)
    elif operation == operators[1]:
        result = float(first) - float(second)
    elif operation == (operators[2]):
        result = float(first) * float(second)
    elif operation == operators[4]:
        result = float(first) / float(second)
    elif operation == "**":
        result = float(first) ** float(second)
    elif operation == "crt":
        result = pow(float(first), 1 / 3)
    elif operation == "sqrt":
        result = square_root(first)
    elif operation == "%":
        result = float(first) % float(second)
    elif operation == "//":
        result = float(first) // float(second)
    elif operation == "<":
        if first < second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed less than " + second)
        else:
            result = (first + " is not less than " + second)
    elif operation == "=":
        if first == second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed equal to " + second)
        else:
            result = (first + " is not equal to " + second)
    elif operation == ">":
        if first > second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed more than " + second)
        else:
            result = (first + " is not more than " + second)
    elif operation == "=/=":
        if first != second:
            result = True
        else:
            result = False
        if result:
            result = (first + " is indeed not equal to " + second)
        else:
            result = (first + " is indeed equal to " + second)
    else:
        result = 0
    return result


def go():
    # getting first number / command
    first = get_first()
    # getting operator
    operation = get_operator()
    # getting second number if operator is not "sqrt"
    second = single_argument_check(operation)
    # the math part
    result = the_actual_math(first, operation, second)
    # print the answer and store it
    print("The answer to your problem is")
    print(str(result))
    print("")
    history.append(result)
    go()


while True:
    helps(starting)
