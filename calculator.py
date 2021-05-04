import numpy as np
history = []
running = False


def calc():
    running = True
    go()


def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


def commands(command1):
    if command1 == "end":
        print("i see you are done")
        print("imma go now ig")
        print("cya")
        quit()
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
        go()
    if not running:
        helps()
    else:
        calc()


def helps():
    print("Command ('start' to start)")
    command = input("> ")
    commands(command)


def go():
    # getting first number / command
    print("First Command / Number")
    first = input("> ")
    if check_float(first):
        pass
    else:
        commands(first)
    # getting operator
    print("Operator")
    operation = input("> ")
    # getting second number if operator is not "sqrt"
    if operation == "sqrt":
        second = 0
        pass
    else:
        print("Second Number")
        second = input("> ")
    # the math part
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
    print("The answer to your problem is")
    print(str(result))
    print("")
    history.append(result)
    calc()


while True:
    helps()
