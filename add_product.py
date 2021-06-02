from main import *

def add_product(p_list):
    print("Please enter the products to be invoiced. do it as follows: (product_name = price).")
    string = input("Add new product: ")
    yes = 'yes'

    tokens = string.split(sep='= ')

    try:
        item = Product(tokens[0], int(tokens[1]))
        p_list.append(item)
        state = True
    except Exception:
        state = False
        print("<Error> You must enter correct values")

    if state is False:
        return add_product(p_list)
    else:
        print("Do you want to continue billing? (yes or no)")
        buy = input()

        if buy == yes:
            return add_product(p_list)
        else:
            billing(p_list)

