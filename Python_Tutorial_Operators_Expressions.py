# Learning Operators and Expressions in Python!
#
# Quick Comparison Operator examples:
## Equality: ==
## Inequality: !=
## Greater Than: >
## Less Than: <
## Greater Than/Equal: >=
## Less Than/Equal: <=
#
# Example of [Equality] Comparison Operator:
print(5 == 5) # Output should be [True]
print(5 == 6) # Output should be [False].
print(5 == 5.0) # Output should be [True].
print(5 == "5") # Output should be [False].
print("Hello" == "Hello") # Output should be [True].
print("Hello" == "hello") # Output should be [False].
print("")
#
# Example of [Inequality] Comparison Operator:
print(5 != 5) # Output should be [False]
print(5 != 6) # Output should be [True].
print(5 != 5.0) # Output should be [False].
print(5 != "5") # Output should be [True].
print("Hello" != "Hello") # Output should be [False].
print("Hello" != "hello") # Output should be [True].
print("")
#
# Example of [Greater Than] Comparison Operator:
print(5 > 5) # Output should be [False]
print(5 > 6) # Output should be [False].
print(5 > 5.0) # Output should be [False].
print(5 > 4) # Output should be [True].
print("Hello" > "hello") # Output should be [False].
print("Hello" > "Hello") # Output should be [False].
print("")
#
# Example of [Less Than] Comparison Operator:
print(5 < 5) # Output should be [False]
print(5 < 6) # Output should be [True].
print(5 < 5.0) # Output should be [False].
print(5 < 4) # Output should be [False].
print("Hello" < "hello") # Output should be [True].
print("Hello" < "Hello") # Output should be [False].
print("")
#
# Example of [Greater Than/Equal] Comparison Operator:
print(5 >= 5) # Output should be [True]
print(5 >= 6) # Output should be [False].
print(5 >= 5.0) # Output should be [True].
print(5 >= 4) # Output should be [True].
print("Hello" >= "hello") # Output should be [False].
print("Hello" >= "Hello") # Output should be [True].
print("")
#
# Example of [Less Than/Equal] Comparison Operator:
print(5 <= 5) # Output should be [True]
print(5 <= 6) # Output should be [True].
print(5 <= 5.0) # Output should be [True].
print(5 <= 4) # Output should be [False].
print("Hello" <= "hello") # Output should be [True].
print("Hello" <= "Hello") # Output should be [True].
print("")
#
# Quick Mathematical Operator examples:
## Addition: +
## Subtraction: -
## Multiplication: *
## Division: /
## Modulus: %
## Exponents: **
#
# Example of [Addition] Math Operator:
print(5 + 5)
print(5 + -5)
print("")
#
# Example of [Subtraction] Math Operator:
print(5 - 5)
print(5 - 4)
print("")
#
# Example of [Multiplication] Math Operator:
print(5 * 5)
print(5 * -5)
print("")
#
# Example of [Division] Math Operator:
print(5 / 5)
print(5 / 2.3)
print("")
#
# Example of [Modulus] Math Operator:
print(5 % 5)
print(5 % 2)
print("")
#
# Example of [Exponents] Math Operator:
print(5 ** 5)
print(5 ** 2)
print("")
#
# Quick Mathematical Assignment Operator examples:
## Addition: +=
## Subtraction: -=
## Multiplication: *=
## Division: /=
## Modulus: %=
## Exponents: **=
#
# Example of [Addition] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign += 20
print(mathAssign)
print("")
#
# Example of [Subtraction] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign -= 20
print(mathAssign)
print("")
#
# Example of [Multiplication] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign *= 20
print(mathAssign)
print("")
#
# Example of [Division] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign /= 20
print(mathAssign)
print("")
#
# Example of [Modulus] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign %= 20
print(mathAssign)
print("")
#
# Example of [Exponents] Math Assignment Operator:
mathAssign = 5
print(mathAssign)
print(mathAssign + 5)
mathAssign = mathAssign + 10
print(mathAssign)
mathAssign **= 20
print(mathAssign)
print("")
#
# Quick Logical Operator examples:
## AND 
## OR
## NOT
#
# Variables:
xVar = 5
yVar = 10
zVar = 32
# Example of [AND] Operator:
print(xVar < yVar and xVar < zVar) # Output should be [True].
print(xVar > yVar and xVar < zVar) # Output should be [False].
print("")
#
# Example of [OR] Operator:
print(xVar < yVar or yVar < zVar) # Output should be [True].
print(xVar > yVar or xVar < zVar) # Output should be [True].
print("")
#
# Example of [NOT] Operator:
print(not(xVar < yVar or yVar < zVar)) # Output should be [False].
print(not(xVar > yVar and xVar < zVar)) # Output should be [True].
print("")
#
# Fun examples of Math Operators with [strings]:
print("Hello" * 3) # Prints Hello 3x.
print("")