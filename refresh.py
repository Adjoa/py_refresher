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

# Loops
for pet in pets:
    print(pet)

for x in range(1,10):
    print(x)
#=> 1 2 3 4 5 6 7 8 9
counter = 0
while counter < 18:
    print(counter)
    counter += 1

# Dictionaries (Hashes, JS Objects)
candies = {"Snickers": 12, "Milky Way": 7, "Starbursts": 5}
print(candies)
print(candies["Milky Way"]) #=> 7
candies["Jolly Ranchers"] = 9
print(candies) #=> {'Snickers': 12, 'Milky Way': 7, 'Starbursts': 5, 'Jolly Ranchers': 9}
del(candies["Starbursts"])
print(candies) #=> {'Snickers': 12, 'Milky Way': 7, 'Jolly Ranchers': 9}

# Classes
class Bunny:
    # bunnyInfo = "Bunnies are cute."

    def __init__(self, name="George", age=0, color="blue"):
        self.name = name
        self.age = age
        self.color = color

    def hop(self, str):
        print("Hop!")

# jelly.hop()
# jelly.name = "Jelly"
# jelly.age = 12
# print(Bunny.bunnyInfo)

jelly = Bunny("Jelly", 12, "purple")
print(jelly.color)