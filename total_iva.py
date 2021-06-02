from main import p_list

def total_iva():
    total  = 0
    total_iva = 0

    for i in p_list:
        total = i.price

    total_iva += ((19 * total) / 100)

    return total_iva