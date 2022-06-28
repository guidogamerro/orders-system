from functions import toEntry


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
