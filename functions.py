def entry(message,error):

    data = input(message)

    while data == "":

        print(error)

        data = input(message)

    return data

def toEntry():

    print("Welcome to GG Burgers")

    name = entry("Enter your name: ","Error, empty field.")

    return name

def intro(name):

    print("GG Burgers")  

    print("Employee: " + name )

def calculate(prices, order):

    total = 0
    total += order["Combo1"] * prices["Combo1"]
    total += order["Combo2"] * prices["Combo2"]
    total += order["Combo3"] * prices["Combo3"]
    total += order["Dessert"] * prices["Dessert"]

    return total