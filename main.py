# Python

# DataType is only check at runtime and not compile time

# Display some text :
print("Hello World")
print('Hello World')

# Variables:
name: str = 'Etienne'
age: int = 28
list = [1, 2, 3, 4]
pi = 3.14
isAdult: bool = True

# Trouver le type de variable:
print(type(age))


# Fonction
def hello() -> str:
    return 'hello'


# I'm a comment

"""
I
am
a
group
of
comments
"""

# String

# length
print(len(name))
# Replace
print(name.replace('E', 'e'))
# UpperCase
print(name.upper())

# Boolean
print(name == 'Etienne')
print(name != 'Etienne')

# Strings of characters into a string or not
print('nn' in name)
print('nn' not in name)

# Multilines String + Input

comment = 'This is a comment ' \
          'but still visible, ' \
          'here it is too'

secondComment = """
Well, now the 
text is multiligne, 
and, that's really 
cool
"""

thirdMultilineComment = """
Hello {}, 
How are you ?
"""
print(comment)
print(secondComment)
print(thirdMultilineComment.format(name))

thirdMultilineComment = f"""
Hello {name}, 
How are you ?
"""
print(thirdMultilineComment.format(name))

# Indentation
# Python is sensitive to indent
# Reserved keywords

#import keywords  # Should be at the beginning of the file

#print(keyword.kwlist)

# Arithmetic operator
# Ctrl + Alt + N to include the result directly into the print
result: int = 1 + 3
print(result)

# Ctrl + D in order to duplicate a line
print(1 + 3)
print(1 * 3)
print(1 / 3)
print(1 % 3)
print(1 - 3)
print(2 ** 3)
print(2 ** 3)

# Comparison Operators
print(10 == 5)
print(10 > 5)
print(10 < 5)
print(10 != 5)
print(10 >= 5)
print(10 <= 5)

# Logical Operators
print(10 > 5 and 1 < 3)
print(10 > 5
      and 1 < 3
      and 'nn' in 'Etienne')
print(10 > 5
      or 1 < 3
      and 'nn' not in 'Etienne')
print(not (
        10 > 5
        or 1 < 3
        and not 'nn' in 'Etienne'))

# Assignment operator
number = 3
number **= 3
number /= 5
number %= 4

# if statements
if number > 0:
    print(f"Number {number} is positive")
elif number == 0:
    print(f"The number is {number}")
else:
    print(f"Number {number} is negative")

# Ternary if statements
message = "positive" if number > 0 else "0 or negative"
print(f"The  number is {message}")

# Lists
numbers = [1, 2, 3, 4, -1, 0, ["A", "B"]]
# Display the list
print(numbers)
# Display one number of the list starting from 0
print(numbers[0])
# Display list from a first list
print(numbers[6][1])

# List methods
numbers = [1, 2, 3, 4, -1, 0]
# Sort a list
numbers.sort()

# Reverse a list
numbers.reverse()

# Add a number
numbers.append(123)
print(numbers)

# Length of the list
length = len(numbers)
print(length)

# Clear the list
numbers.clear()

# Check if a value is include within a list
includedIntoList = 5 in numbers
print(includedIntoList)

# Delete an item from a list
numbers = [1, 2, 3, 4, -1, 0, 1, 1, 2, 3, 1, 1, -1]
numbers.remove(1)
# Deleting the last index
numbers.pop()
# Deleting a specific index
del numbers[0]
# Deleting a range of index (last param excluded)
del numbers[1:6]
print(numbers)

# Sets
numbersList = [1, 1]
numbersSet = {1, 1}
lettersSet = {"A", "A", "B", "C", "C"}

print(numbersList)
print(numbersSet)  # result : {1}
print(lettersSet)  # No duplication

lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "F", "G", "H"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB  # The order is important
print(union)
print(intersection)
print(difference)

# /Dictionaries
# Dictionaries stores key/values pairs

person = {
    "name": "Etienne",
    "age": 28,
    "gender": "male"
}

# Keys have to be unique
print(person["name"])
print(person["age"])
print(person["gender"])
print(person.keys())
print(person.values())
print(person.get("age"))

person["age"] = 27
print(person["age"])

# Loops

names = ["Etienne", "Ha", "Etienne", "Elise"]

for name in names:
    print(name)

# Loop through dictionaries
# array of key/value pairs
print(person.items())

for key in person:
    print(f"key: {key} ; value: {person[key]}")

for key, value in person.items():
    print(f"key: {key} ; value: {value}")

# While loop

number = 0

while number < 10:
    print(number)
    number += 1
else:
    print("While loop ended")

# Break and Continue

number = 0

while number < 10:
    if number == 5:
        print(f"Number is {number}")
        break
    print(number)
    number += 1

for n in [1, 2, 3, 4, 5]:
    if n < 5:
        continue
    print(n)

while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)


# Functions

def greet(name: str, age=-1):
    print(f"Hello {name}")
    if not age < 0:
        print(f"I know your age = {age} ")


def isAdult(age):
    if age > 15:
        return True
    else:
        return False


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender \"{gender}\" is unknown"


greet("Etienne", 28)
greet("Jacques")

print(isAdult(16))

print(convertGender("M"))
print(convertGender("m"))
print(convertGender("F"))
print(convertGender("f"))
print(convertGender("hello"))

# Modules

import math

print(math.pi)

from math import isqrt

print(isqrt(65))

# Creating Modules

import calculator
from calculator import add
from calculator import multiply
from calculator import substract
from calculator import divide

print(add(5, 7))
print(divide(5, 7))
print(multiply(5, 7))
print(substract(5, 7))
print(calculator.add(5, 7))
print(calculator.divide(5, 7))
print(calculator.multiply(5, 7))
print(calculator.substract(5, 7))


# Classes & Objects

class Phone:

    # init = constructor : it's how you create your phone
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    # Printing Objects
    # The arrow means it returns a str datatype
    def __str__(self) -> str:
        return f"Brand = {self.brand}\nPrice = {self.price}"


iPhone = Phone("Apple", 300)
samsung = Phone("Samsung", 400)

print(iPhone)
print(iPhone.brand)
print(iPhone.price)
iPhone.call(999)

print(samsung)
print(samsung.brand)
print(samsung.price)
samsung.call(999)

# Working with date

import datetime
from datetime import datetime
from datetime import date

# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.now().time())

print(datetime.now())
print(datetime.now().date())
print(datetime.now().year)
print(datetime.now().day)
print(date.today())
print(datetime.now().time())

# Formatting dates

now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))
print(date.today().strftime("%d/%m/%Y"))
print(date.today().strftime("%d-%B-%Y"))
print(date.today().strftime("%d-%b-%Y"))

# Creating Files

# The mode is open / read / append / ...the file
# w writting, a appending, r reading, r+ reading/writing
file = open("./data.csv", "w")
file.write("id, name, email\n")
file.write("1, Etienne, etienne.b@mail.com\n")
file.write("2, Ha, ha.p@mail.com\n")
file.close()
file = open("./data.csv", "a")
file.write("3, Jacques, j.b@mail.com\n")
file.close()
# file = open("./data.csv", "r+")
# file.write("3, Jacques, j.b@mail.com\n")
# file.close()

# Reading from file

file = open("./data.csv", "r")
# print(file.read())
# for line in file:
#     print(line)

print(file.readlines())
file.close()

import os.path

fileName = "data.csv"
if os.path.isfile(fileName):
    # Automaticaly closes the file
    with open("./data.csv", "r") as file:
        print(file.read())
else:
    print(f"The file {fileName} does not exist")

# Pip and Modules

# Fetching data from internet

from urllib import request
import requests
import json
import pyttsx3

r = request.urlopen("https://www.google.com")
print(r)
print(r.getcode())
print(r.read())


# Fetching jokes from internet

# class must be before any call (the file is read lineary
class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"{self.setup}\n{self.punchline}\n"


jokes = []

url = "http://official-joke-api.appspot.com/random_ten"

r = request.urlopen(url)
data = r.read()

jsonData = json.loads(data)
print(jsonData)

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"There are {len(jokes)} jokes")

for joke in jokes:
    print(joke)

jokesBis = []
urlBis = "http://official-joke-api.appspot.com/random_joke"
# pip3 install requests
response = requests.get(urlBis)
dataBis = response.text
print(response.status_code)

jsonDataBis = json.loads(dataBis)
print(jsonDataBis)

setup = jsonDataBis["setup"]
punchline = jsonDataBis["punchline"]
jokeBis = Joke(setup, punchline)
jokesBis.append(jokeBis)

print(f"There are {len(jokesBis)} more jokes")

for joke in jokesBis:
    print(joke)

# Text To Speech
# pip3 install pyttsx3

pyttsx3.speak("Etienne")

for joke in jokesBis:
    pyttsx3.speak(joke.setup)
    pyttsx3.speak(joke.punchline)
