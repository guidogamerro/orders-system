import sqlite3

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

def intNumber(message, error):

    data = input(message)

    while True:

        try:

            data = int(data)

            break

        except ValueError:

            print("Error")

            data = input(message)

    return data

def saveSale(data):

    '''row = ""

    for n in data:

        if n == "Total":

            row += str(data[n]) + "\n"

        else:

            row += str(data[n]) + ","

    f = open("Sales.txt","a")

    f.write(row)

    f.close()'''

    datas = tuple(data.values())

    conn = sqlite3.connect("shop.sqlite")

    cursor = conn.cursor()

    try:

        cursor.execute("INSERT INTO sales VALUES (null, ?, ?, ?, ?, ?, ?, ?)", datas)

    except sqlite3.OperationalError:

        cursor.execute("""CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client TEXT,
            date TEXT,
            combo1 INT,
            combo2 INT,
            combo3 INT,
            desserts INT,
            total INT
        )""")
        cursor.execute("INSERT INTO sales VALUES (null, ?, ?, ?, ?, ?, ?, ?)", datas)
    
    conn.commit()

    conn.close()

    print("Contact salved")

def saveOperator(data):

    entry = "IN " + data["Entry"] + " Operator " + data["Name"] + "\n"

    exit = "OUT " + data["Exit"] + " Operator "+ data["Name"] +" $ " + str(data["Money"]) + "\n"

    separator = ("#" * 50) + "\n"

    f = open("Register.txt","a")

    f.write(entry)

    f.write(exit)

    f.write(separator)

    f.close()