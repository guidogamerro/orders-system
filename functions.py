def entry(message,error):

    data = input(message)

    while data == "":

        print(error)

        data = input(message)

    return data

def toEntry():

    print("Welcome to GG Burgers")

    name = entry("Enter your name: " , "Error, empty field.")

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

def confirm():

    answer = entry("Do you confir the order? Y/N" , "Error, empty field")

    while answer.lower() != "y" and answer.lower() != "n" and answer.lower() != "yes" and answer.lower() != "no":

        print("Enter only yer or no")

        answer = entry("Do you confir the order? Y/N" , "Error, empty field")

    if answer == "y" or answer == "yes":

        return True

    else:

        return False