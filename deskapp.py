import tkinter as tk
from typing import Text

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

window.mainloop()