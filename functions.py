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