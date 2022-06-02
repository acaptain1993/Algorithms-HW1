
def split_rearrange_string():
    user_string = input(print("Please enter a string: "))
    number_of_chars = len(user_string)
    part_one = user_string[:number_of_chars // 2]
    part_two = user_string[number_of_chars // 2:]
    remix_string = part_two + part_one
    print(remix_string)


def unique_char():
    user_string = input(print("Please enter a string: "))
    unique_finder = list((set(user_string)))
    true_or_false = bool(len(user_string) == (len(unique_finder)))
    print(true_or_false)


split_rearrange_string()
unique_char()
