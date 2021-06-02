from tkinter import *

def add():
    print(name.get() + '\n' + price.get())


root=Tk()
root.title("Invoice")
root.geometry('800x500')
root.configure(background='grey')

name = StringVar()
price = StringVar()

name.set()
price.set()

text_name = Label(root, text="Write here the name of the product: ", bg="#45B39D", fg="black")
text_name.place(x=10, y=10)
entry_name = Entry(root, textvariable=name)
entry_name.place(padx=5, pady=5, ipadx=5, ipady=5, fill=X)

text_price = Label(root, text="Write here the price of the product: ", bg="#45B39D", fg="black")
text_price.place(x=10, y=40)
entry_name = Entry(root, textvariable=price)
entry_name.place(padx=5, pady=5, ipadx=5, ipady=5, fill=X)


agregar = Button(root, text="Add/Agregar", command=add)
agregar.place(x=10, y=10)

root.mainloop()