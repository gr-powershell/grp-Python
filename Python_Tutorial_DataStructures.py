# Learning Data Structures in Python!
#
# A data structure is a particular way of organizing
# data in a computer so that it can be used effectively.
#
# Lists: Data structure in Python that is a mutable, or
# changeable, ordered sequence of elements. Each element
# or value within a list is called an [item]. Lists are
# defined as having values between square brackets [].
## [val1, val2, val3]
#
# Empty List:
myList = []
print(type(myList))
print("")
#
# List with values:
myList = [1, "two", 3.14, False]
print(type(myList))
print(myList)
print("")
#
# Referencing items in the List:
print(myList[0]) # All items in a List start with Index [0]!
print(myList[1])
print(myList[2])
print(myList[3])
print("")
#
# Changing items in the List:
print(myList[1])
myList[1] = "three"
print(myList[1])
print("")
#
# Adding items to the List:
myList.append("new item") # Append and item to a List by using the [.append] method.
print(myList)
print(len(myList))
print("")
#
# Deleting items from the List:
myList.pop()[4]
print(myList)
# OR
myList.remove(1)
print(myList)
#
# Recreate the original List:
myList = [1,"three", 3.14, False, "new item"]
print(myList)
print("")
#
# Dictionaries: An unordered collection of data values,
# used to store data values like a map. Very similar to
# hash tables in PowerShell.
## Dictionary holds [key:value]
#
# Empty Dictionary:
myDict = {}
print(type(myDict))
print("")
#
# Dictionary with values:
myDict = {'name': 'Greg','age': 32}
print(myDict)
print("")
#
# Reference items in the Dictionary:
print(myDict['name'])
print(myDict['age']) # Need to reference the [key] to print the [value]!
print("")
#
# Changing items in the Dictionary:
myDict['name'] = "Gregory"
print(myDict)
print("")
#
# Adding items to the Dictionary:
myDict['weight'] = 230
print(myDict)
myDict['height'] = "5'10"
print(myDict)
print("")
#
# Deleting items from the Dictionary:
print(myDict)
del myDict['height']
print(myDict)
print("")
#
# Practice Dictionary exercise:
Address = {'houseNumber': 5, 'streetName': "Oak Street", 'city': "Testville", 'state': "MA"}
print(type(Address))
print(Address)
print(Address['houseNumber'])
print(Address['streetName'])
print(Address['city'])
print(Address['state'])
print("I currently live at " + str(Address['houseNumber']) + " " + Address['streetName'] + ", " + Address['city'] + ", " + Address['state'] + ".")
Address['zipCode'] = 12345
print(Address['zipCode'])
print("I currently live at " + str(Address['houseNumber']) + " " + Address['streetName'] + ", " + Address['city'] + ", " + Address['state'] + " " + str(Address['zipCode']) + ".")
print("")
#
# Tuple: A sequence of immutable Python objects. Tuples
# are sequences, just like [Lists]. Difference being,
# Tuples cannot be changed and use parentheses (),
# whereas [Lists] use square brackets [].
#
# Empty Tuple:
myTuple = ()
print(type(myTuple))
print("")
#
# Tuple with values:
myTuple = (1, "two", 3.14, False)
print (myTuple)
print("")
#
# Referencing items in the Tuple:
print(myTuple[1])
print("")
#
# Changing items in the Tuple:
# NOPE!
#
# Adding items to the Tuple:
# NOPE!
#
# Deleting items from the Tuple:
del myTuple # Need to delete the whole Tuple! Cannot delete single items!
#
# Sets: A collection which is unordered and unindexed. In
# Python, sets are written with curly brackets (like a Dictionary
# but without the key).
#
# Empty Set:
mySet = set({}) # Built like a Dictionary, but needs to be type cast with set()!
print(type(mySet))
print("")
#
# Set with values:
mySet = {1, "two", 3.14, False}
print(mySet)
print("")
#
# Referencing items in the Set:
# NOPE! But can work with items in a Set within a For Loop.
#
# Changing items in the Set:
# NOPE!
#
# Adding items to the Set:
mySet.add("new item")
print(mySet)
print("")
#
# Deleting items from the Set:
mySet.remove("new item")
print(mySet)