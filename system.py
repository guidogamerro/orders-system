from functions import toEntry, entry

prices = {"Combo1" : 5 , "Combo2" : 6 , "Combo3" : 7 , "Dessert" : 2}

exit = True

while exit:

    operatorData = {"Name" : "" , "Entry" : "" , "Exit" : "" , "Money" : 0}

    operator = toEntry()

    #start = time.asctime()

    operatorData["Name"] = operator

    #operatorData["Entry"] = start

    #cashRegister = 0

    #print("\n\n")

    while True:

        intro = operator

        print("""
        1 - Ingreso de nuevo pedido
        2 - Cambio de turno
        3 - Apagar sistema
        """)

        option = entry("number", "Error, empty field")

        if option == "1":

            #print("\n\n")

            order = {"Client" : "" , "date":"" , "Combo1" : 0 , "Combo2" : 0 , "Combo3" : 0 , "Dessert" : 0 , "Total" : 0}
            order["Client"] = entry("Client's name: ", "Error, empty field")
            #order["date"] =
            #order["Combo1"] =
            #order["Combo2"] =
            #order["Combo3"] =
            ##order["Dessert"] =
            ##order["Total"] =