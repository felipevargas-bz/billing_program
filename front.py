from add_product import add_product
from main import *
from print_invoice import print_invoice
from total_invoice import total_invoice
from total_discounts import total_discounts
from total_iva import total_iva
from clear_all import clear_all
from tkinter import *

def add():
    p_list.append(add_product(name.get(), price.get()))
    t_invoice.set(str(total_invoice()))
    t_iva.set(str(total_iva()))
    t_discouts.set(str(total_discounts()))



root=Tk()
root.title("Invoice")
root.geometry('400x400')
root.resizable(False, False)
root.configure(background='grey')

name = StringVar()
price = StringVar()
t_invoice = StringVar()
t_iva = StringVar()
t_discouts = StringVar()

name.set("")
price.set("")

text_name = Label(root, text="Write here the name of the product: ", bd=2,\
     bg="#AEB6BF", fg="black", font="Curier 10")
text_name.grid(row=0, column=0)
entry_name = Entry(root, textvariable=name, bd=3)
entry_name.grid(row=0, column= 1)

text_price = Label(root, text="Write here the price of the product: ", bd=2, \
    bg="#AEB6BF", fg="black", font="Curier 10")
text_price.grid(row=3, column=0)
entry_price = Entry(root, textvariable=price, bd=3)
entry_price.grid(row=3, column=1)


push_product = Button(root, text="Add product", command=add, font="Curier 10")
push_product.place(x=260, y=50)


text_invoice = Label(root, text="Total invoice: ", bd=2, \
    bg="#AEB6BF", fg="black", font="Curier 10")
text_invoice.place(x=10, y=180)
entry_invoice = Entry(root, textvariable=t_invoice, font="Curier 10", bd=5, state="disable")
entry_invoice.place(x=10, y=200)

text_invoice = Label(root, text="Total IVA: ", bd=2, \
    bg="#AEB6BF", fg="black", font="Curier 10")
text_invoice.place(x=10, y=240)
entry_invoice = Entry(root, textvariable=t_iva, font="Curier 10", bd=5, state="disable")
entry_invoice.place(x=10, y=260)

text_invoice = Label(root, text="Total discounts: ", bd=2, \
    bg="#AEB6BF", fg="black", font="Curier 10")
text_invoice.place(x=10, y=300)
entry_invoice = Entry(root, textvariable=t_discouts, font="Curier 10", bd=5, state="disable")
entry_invoice.place(x=10, y=320)


p_invoice = Button(root, text="print invoice", command=print_invoice, font="Curier 10")
p_invoice.place(x=300, y=350)

clean_up = Button(root, text="Clear all", command=clear_all, font="Curier 10")
clean_up.place(x=230, y=350)

root.mainloop()
