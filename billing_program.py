

class Product:

    def __init__(self, name, value):
        self.name = name
        self.value = value


def discounts(p_list, total):
    IVA = ((19 * total) / 100)
    yes = 'yes'
    discount = 0
    subtotal = (total + IVA)
    discount_products_index = []

    if subtotal < 100000:
        print("No discounts will be applied.")
        state = input("Do you want to continue billing? (yes or no): ")

    elif subtotal >= 100000 and subtotal <= 200000:
        index = 0
        subtotal = 0

        while index < len(p_list):
            if p_list[index].value > 20000:
                discount += ((5 * p_list[index].value) / 100)
            else:
                subtotal += p_list[index].value
            index += 1
        subtotal += discount
        subtotal = (subtotal + ((19 * subtotal) / 100))

        state = input("Do you want to continue billing? (yes or no): ")
    else:
        subtotal = (total + ((10 * total) / 100))
        subtotal += IVA
        state = input("Do you want to continue billing? (yes or no): ")
    
    if state == yes:
        return add_product(p_list)
    else:
        print("The total of the invoice is: {}".format(subtotal))
        print("Total discounts: {}".format(discount))


def billing(p_list):
    index = 0
    total = 0

    while index < len(p_list):
       total += p_list[index].value
       index += 1

    discounts(p_list, total)



def main():
    p_list = []
    add_product(p_list)

if __name__ == "__main__":
    main()

