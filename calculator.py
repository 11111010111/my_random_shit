import numpy as np
history = []
running = False
operators = ["+", "-", "*", "/", "**", "sqrt", "%"]


def calc():
    running = True
    go()


def end():
    print("i see you are done")
    print("imma go now ig")
    print("cya")
    quit()


def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


def commands(command1):
    if command1 == "end":
        end()
    elif command1 == "help":
        print("The commands are:")
        print("history, end, help, command")
        print("History: shows all results")
        print("End: ends program")
        print("Help: shows all commands")
        print("Command: goes back to starting prompt")
    elif command1 == "history":
        print(history)
    elif command1 == "start":
        print("Lets go!!")
        calc()
    elif command1 == "command":
        helps()
    else:
        print("Please enter a valid command")
        helps()
    if not running:
        helps()
    else:
        calc()


def com(command1):
    if command1 == "command":
        helps()
    elif command1 == "end":
        end()
    else:
        print("Not a valid integer/float")
        print("Please try again")
        go()


def helps():
    print("Command ('start' to start)")
    command = input("> ")
    commands(command)


def get_first():
    print("First Command / Number")
    first = input("> ")
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
        get_operator()
    return operation


def sqrt_check(operation):
    if operation == "sqrt":
        second = 0
        pass
    else:
        print("Second Number")
        second = input("> ")
    return second


def the_actual_math(first, operation, second):
    if operation == "+":
        result = float(first) + float(second)
    elif operation == "-":
        result = float(first) - float(second)
    elif operation == "*":
        result = float(first) * float(second)
    elif operation == "/":
        result = float(first) / float(second)
    elif operation == "**":
        result = float(first) ** float(second)
    elif operation == "sqrt":
        result = np.sqrt(float(first))
    elif operation == "%":
        result = float(first) % float(second)
    else:
        print("You need to put an operator (+, -, *, /, **, sqrt) in the operator prompt")
        result = "Please try again"
    return result


def go():
    # getting first number / command
    first = get_first()
    # getting operator
    operation = get_operator()
    # getting second number if operator is not "sqrt"
    second = sqrt_check(operation)
    # the math part
    result = the_actual_math(first, operation, second)
    # print the answer and store it
    print("The answer to your problem is")
    print(str(result))
    print("")
    history.append(result)
    calc()


while True:
    helps()
