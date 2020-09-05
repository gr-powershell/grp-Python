# Learning Conditional Execution and Control Flow in Python!
#
# Conditional Execution: IF something is true, do something.
# ELSE IF something else is true, do something else. ELSE
# if nothing above was true, do something.
#
# Example of the [if] statement:
COLOR = "blue"
if COLOR == "blue":
    print("The statement matched the color [blue]")
print("")
#
# Example of the [if] statement with the variable set to input:
COLOR = input("What is your favorite color?: ")
if COLOR == "blue":
    print("The statement matched the color [blue].")
print("")
#
# Example of the [elif] statement (You need the [if] or else the
# [elif] cannot be used!):
COLOR = input("What is your favorite color?: ")
if COLOR == "blue":
    print("The statement matched the color [blue]")
elif COLOR != "blue":
    print("The statement did NOT match the color [blue]")
print("")
#
# Example of adding an [else] to the current statement (Can only
# have one, [if] and only one [else]!):
COLOR = input("What is your favorite color?: ")
if COLOR == "blue":
    print("The statement matched the color [blue]")
elif COLOR == "red":
    print("The statement matched the color [red]")
else:
    print("The statement did NOT match the colors [blue] or [red]!")
print("")