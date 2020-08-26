# Learning Data Types in Python!
#
## Strings [List of characters.]
## Int(egers) [Whole numbers.]
## Booleans [True/False]
## Floats/Doubles [Decimal numbers.]
#
# Type Casting: Deliberately specify the [type] on a variable.
## int(), str(), float()
#
# Normal print() command of a [string]:
print("My name is Greg!")
print("")
#
# In order to Type Cast a valid [string] to an [int]:
print(int("300"))
print("")
#
ANSWER = input("Please enter a number: ")
print(ANSWER, type(ANSWER))
# OR
print(type(ANSWER))
print("")
#
# The output above is of type [string]. In order to use that value with an [int],
# do the following: (Example of simple addition, converting the ANSWER variable
# from [string] to [int].)
print(10 + int(ANSWER))
print("")
#
# The following would need to have the variable [totalExpenses] type cast
# to a [string] in order to be able to concatenate within the print() statement below:
totalExpenses = 750
print("Your total expenses for the month were $" + str(totalExpenses) + " this month.")
# OR
print(f"Your total expenses for the month were ${totalExpenses} this month.")
# OR
print("Your total expenses for the month were ${} this month.".format(totalExpenses))
print("")
#
# Type casting an [int] to a [float]:
print(float(5))
print("")
#
# Type casting a [string] to a [float]:
print(float("10"))
print("")
#
# String Methods: Built in functions to help you with formatting of [strings].
# https://www.w3schools.com/python/python_ref_string.asp
#
# The example below uses the capitalize() method, which will capitalize the first
# letter of the [string]:
print("hello".capitalize())
#
# The example below uses the casefold() method, which will convert the [string] to
# lower case:
print("Hello".casefold())
#
# The example below uses the split() method, which will split a [string] into
# a [list] where each word is an item in the [list]:
print("My name is Greg!".split())
print("")
#
# Mathmatical Functions
#
## import math ##
## Round up (ceil)
## Round down (floor)
## Absolute value (fabs) -- A number can never be negative!
## Sum (fsum)
## Exponents (pow)
#
import math # This imports the [math] package, including all related functions.
#
# Using the NUM variable, (math.ceil) will be to round the variable
# data [4.6] UP, to, [5].
NUM = 4.6
print(math.ceil(NUM))
#
# Using the NUM variable, (math.floor) will be to round the variable
# data [4.6] DOWN, to [4].
print(math.floor(NUM))
#
# Using the NUMS variable, (math.fsum) will add together all of the
# values within NUMS.
NUMS = [8.5, 20, 34.7, 14.3, 87.4]
print(math.fsum(NUMS))
#
# The (math.pow) function below, takes both values [2,2] and performs
# 2 to the power of 2.
print(math.pow(2,2))
print("")
#
# None Type: None is NOT the same as False! None is NOT 0! None is NOT
# and empty string! Comparing None to anything will always return False
# except None itself.
#
VAR = None
print(type(None))