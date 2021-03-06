from functions import confirm, saveOperator, toEntry, entry, intNumber, calculate, saveSale
import time
import os

if (os.name == "nt"):

    erase = "cls"

else:

    erase = "clear"

prices = {"Combo1" : 5 , "Combo2" : 6 , "Combo3" : 7 , "Dessert" : 2}

exitSys = True

os.system(erase)

while exitSys:

    os.system(erase)

    operatorData = {"Name" : "" , "Entry" : "" , "Exit" : "" , "Money" : 0}

    operator = toEntry()

    start = time.asctime()

    operatorData["Name"] = operator

    operatorData["Entry"] = start

    cashRegister = 0

    os.system(erase)

    print("\n\n")

    while True:

        intro = operator

        print("""
        1 - Ingreso de nuevo pedido
        2 - Cambio de turno
        3 - Apagar sistema
        """)

        option = entry("Option number ", "Error, empty field")

        if option == "1":

            print("\n")

            order = {"Client" : "" , "Date":"" , "Combo1" : 0 , "Combo2" : 0 , "Combo3" : 0 , "Dessert" : 0 , "Total" : 0}
            order["Client"] = entry("Client's name: ", "Error, empty field")
            order["Combo1"] = intNumber("Amount of Combo1: ", "Error, only numbers")
            order["Combo2"] = intNumber("Amount of Combo2: ", "Error, only numbers")
            order["Combo3"] = intNumber("Amount of Combo3: ", "Error, only numbers")
            order["Dessert"] = intNumber("Amount of desserts: ", "Error, only numbers")

            total = calculate(prices, order)
            print("Total is: $", total)

            payment = intNumber("Pay with: ", "Error, only numbers")

            while total > payment:

                print("It is not enough, your payment must be greater than the total")

                payment = intNumber("Pay with: ", "Error, only numbers")

            print("Change $" , payment - total)

            condition = confirm()     

            if condition:

                cashRegister += total

                order["Date"] = time.asctime()

                order["Total"] = total

                saveSale(order)

            else:

                print("Order was cancelled")

        elif option == "2":

            operatorData["Exit"] = time.asctime()

            operatorData["Money"] = cashRegister

            saveOperator(operatorData)

            break

        elif option == "3":

            operatorData["Exit"] = time.asctime()

            operatorData["Money"] = cashRegister

            saveOperator(operatorData)

            print("Thank you, see you later")

            exitSys = False

            break

        else:

            print("Wrong option, try again")

            print("\n*2")
        
        os.system(erase)