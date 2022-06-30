import sys
import tkinter as tk
from typing import Text
from tkinter import messagebox
import time
from functions import saveOperator, saveSale

#FUNCTIONS

def erase2():

    combo122.delete(0, tk.END)
    combo222.delete(0, tk.END)
    combo322.delete(0, tk.END)
    dessert22.delete(0, tk.END)
    client22.delete(0, tk.END)

def orderCancel():

    answer = messagebox.askyesno(title = "Question", message = "Do you want to cancel the order?")

    if answer:

        erase2()

def exit():

    answer = messagebox.askyesno(title = "Question", message = "Do you wan to exit?")

    if answer:

        operatorData["Exit"] = time.asctime()
        saveOperator(operatorData)
        sys.exit()

def order():

    amount1 = int(combo122.get())
    #validar
    amount2 = int(combo222.get())
    #validar
    amount3 = int(combo322.get())
    #validar
    amountD = int(dessert22.get())
    #validar

    if amount1 >= 0 and amount2 >= 0 and amount3 >= 0 and amountD >= 0:

        client = client22.get()
        operator = operator22.get()

        if client and operator:

            answer = messagebox.askyesno(title = "Question", message = "Confirm order?")

            if answer:

                total = amount1 * prices["Combo1"] + amount2 * prices["Combo2"] + amount3 * prices["Combo3"] + amountD * prices["Dessert"]
                date = time.asctime()
                #trying
                order = {"Client" : "" , "Date":"" , "Combo1" : 0 , "Combo2" : 0 , "Combo3" : 0 , "Dessert" : 0 , "Total" : 0}
                order["Client"] = client
                order["Date"] = date
                order["Combo1"] = amount1
                order["Combo2"] = amount2
                order["Combo3"] = amount3
                order["Dessert"] = amountD
                order["Total"] = total
                #order = [client, date, amount1, amount2, amount3, amountD, total]
                messagebox.showinfo(title = "To pay", message = "$" + str(total))
                saveSale(order)
                messagebox.showinfo(title = "Information", message = "Successful order")

                if operatorData["Name"] != operator and operatorData["Exit"] == "":

                    operatorData["Name"] = operator
                    operatorData["Exit"] = "No date"
                    operatorData["Money"] += total

                elif operatorData["Name"] == operator:

                    operatorData["Money"] += total

                else:

                    operatorData["Exit"] = date
                    saveOperator(operatorData)
                    operatorData["Name"] = operator
                    operatorData["Entry"] = date
                    operatorData["Money"] = 0
                    operatorData["Money"] += total

                erase2()

            else:

                messagebox.showinfo(title = "Information", message = "Order is paused")
            
        else:

            messagebox.showinfo(title = "Wanrnig", message = "Error, enter correct data")
        
    else:

        messagebox.showinfo(title = "Wanrnig", message = "Error, enter correct data")



##DESK APP

operatorData = {"Name" : "" , "Entry" : "" , "Exit" : "" , "Money" : 0}
prices = {"Combo1" : 5 , "Combo2" : 6 , "Combo3" : 7 , "Dessert" : 2}

window = tk.Tk()

window.config(width = 450, height = 450)

window.title("Order system")

#LABELS

intro2 = tk.Label(text = "Order")
intro2.place(x = 175, y = 30)

operator2 = tk.Label(text = "Operator")
operator2.place(x = 60, y = 70)

combo12 = tk.Label(text = "Combo 1")
combo12.place(x = 60, y = 120)

combo22 = tk.Label(text = "Combo 3")
combo22.place(x = 60, y = 170)

combo32 = tk.Label(text = "Combo 3")
combo32.place(x = 60, y = 220)

dessert2 = tk.Label(text = "Desserts")
dessert2.place(x = 60, y = 270)

client2 = tk.Label(text = "Client")
client2.place(x = 60, y = 320)

#BOXES

operator22 = tk.Entry()
operator22.place(x = 150, y = 70)

combo122 = tk.Entry()
combo122.place(x = 150, y = 120)

combo222 = tk.Entry()
combo222.place(x = 150, y = 170)

combo322 = tk.Entry()
combo322.place(x = 150, y = 220)

dessert22 = tk.Entry()
dessert22.place(x = 150, y = 270)

client22 = tk.Entry()
client22.place(x = 150, y = 320)

#BUTTONS

order22 = tk.Button(text = "Order", command = order)
order22.place(x = 50, y = 370, height = 30, width = 80)

cancel22 = tk.Button(text = "Cancel", command = orderCancel)
cancel22.place(x = 170, y = 370, height = 30, width = 80)

exit22 = tk.Button(text = "Exit", command = exit)
exit22.place(x = 290, y = 370, height = 30, width = 80)

window.mainloop()