class Product:

    def __init__(self, name, value):
        self.name = name
        self.value = value
def add_product(list):
    string = input("Add new product: ")
    yes = 'yes'
    no = 'no'

    tokens = string.split(sep='= ')

    try:
        item = Product(tokens[0], int(tokens[1]))
        list.append(item)
        state = True
    except Exception:
        state = False
        print("<Error> You must enter correct values")

    if state is False:
        return add_product(list)
    else:
        print("Do you want to continue billing? (yes or no)")
        buy = input()

        if buy == yes:
            return add_product(list)
        else:
            index = 0
            while (index < len(list)):
                print("name: {}, price: {}".format(list[index].name, list[index].value))
                index += 1

def main():
    list = []
    print("Please enter the products to be invoiced. do it as follows: (product_name = price).")
    add_product(list)

if __name__ == "__main__":
    main()

