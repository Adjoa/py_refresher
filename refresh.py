# Hello, world!
print("Hello, world!")

# Variables, Strings, Ints, and Print
name = "Adjoa"
age = 2000

print("Hello, world! My name is {}, and I am {} years old.".format(name, age))

# If Statements and Comments
isHot = True

if isHot:
    print("Hace calor!")
else:
    print("Hace frio.")

if name == "Julie":
    print("The name is Julie.")

if age > 2000:
    print("Age is greater than 2000")

"""
This is a 
multi-line 
comment!
"""

# Functions
def hello():
    print("Hello, world.")

hello()
hello()
hello()

def helloSomebody(name="Delia"):
    return "Hello, {}.".format(name)

greetingOne = helloSomebody("Marge")
greetingTwo = helloSomebody()
print(greetingOne)
print(greetingTwo)

# Lists (Arrays)
pets = ["Spot", "Fred", "McGee", "Polly"]
print(pets) #=> ["Spot", "Fred", "McGee", "Polly"]\

pets.insert(0, "Goldie")
print(pets) #=> ["Goldie", "Spot", "Fred", "McGee", "Polly"]

del(pets[2])
print(pets) #=> ["Goldie", "Spot", "McGee", "Polly"]
print(pets[2]) #=> McGee
print(len(pets)) #=> 4

pets[3] = "Jacks"
print(pets) #=> ["Goldie", "Spot", "McGee", "Jacks"]

