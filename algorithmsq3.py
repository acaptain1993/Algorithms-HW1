user_number = input(print("Please enter any number"))
user_number_int = int(user_number)
user_len = len(user_number)
user_len_int = int(user_len)
loop_counter = 1
current_digit = 0
even_numbers = 0
odd_numbers = 0
while loop_counter <= user_len_int:
    if int(user_number[current_digit]) % 2 == 0:
        even_numbers = even_numbers + 1
        current_digit = current_digit + 1
    elif int(user_number[current_digit]) % 2 != 0:
        odd_numbers = odd_numbers + 1
        current_digit = current_digit + 1
    loop_counter = loop_counter + 1

print(f"There are {even_numbers} even numbers and {odd_numbers} odd numbers.")

