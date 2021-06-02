from add_product import add_product
from tkinter import *

root=Tk()

root.title("Invoice")

root.geometry("1080x600")

agregar = Button(root, text="Add/Agregar", command=add_product)

root.mainloop()

