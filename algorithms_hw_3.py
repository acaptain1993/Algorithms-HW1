def below_the_arithmetical_mean():
    start_list = [6, 12, 55, 23, 7, 13]
    list_item_number = len(start_list)
    item_total = 0
    for item in start_list:
        item_total = item + item_total

    item_mean = item_total / list_item_number
    final_list = []
    for number in start_list:
        if number < item_mean:
            final_list.append(number)

    print(f"The mean of the list is {item_mean}")
    print(f"The new list is:\n {final_list}")


def two_lowest_items():
    start_list = [6000, 210, 55, 74, 140, 87, 43]
    final_list = []
    for item in start_list:
        if item == start_list[0]:
            lowest_number = item
            lowest_number_two = item
        if item <= lowest_number_two and item <= lowest_number:
            lowest_number_two = lowest_number
            lowest_number = item
        elif item <= lowest_number_two and item > lowest_number:
            lowest_number_two = item

    final_list.append(lowest_number)
    final_list.append(lowest_number_two)
    print(f"This is the list with only the two lowest numbers\n {final_list}")


below_the_arithmetical_mean()
two_lowest_items()
