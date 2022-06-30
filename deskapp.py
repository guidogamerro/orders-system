import tkinter as tk
from typing import Text
from tkinter import messagebox

#FUNCTIONS

def erase2():

    combo122.delete(0, tk.END)
    combo222.delete(0, tk.END)
    combo322.delete(0, tk.END)
    dessert22.delete(0, tk.END)
    client22.delete(0, tk.END)

def orderCancel():

    answer = messagebox.askyesno(title = "Question", message = "Do you wan to cancel the order?")

    if answer:

        erase2()

##DESK APP

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

order22 = tk.Button(text = "Order")
order22.place(x = 50, y = 370, height = 30, width = 80)

cancel22 = tk.Button(text = "Cancel", command = orderCancel)
cancel22.place(x = 170, y = 370, height = 30, width = 80)

exit22 = tk.Button(text = "Exit")
exit22.place(x = 290, y = 370, height = 30, width = 80)

window.mainloop()