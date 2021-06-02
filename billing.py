from discounts import discounts


def billing(p_list):
    index = 0
    total = 0

    while index < len(p_list):
       total += p_list[index].value
       index += 1

    discounts(p_list, total)
