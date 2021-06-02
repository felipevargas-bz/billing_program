from main import p_list

def total_invoice():
    sub_total = 0
    total = 0

    for i in p_list:
        sub_total += i.price

    total = (sub_total + ((19 * sub_total) / 100))
    
    return total