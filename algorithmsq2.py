number_one = int(input(print("Enter first number: ")))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

highest_number = 0
higher_of_one_two = 0

if number_one > number_two:
    higher_of_one_two = number_one
elif number_two > number_one:
    higher_of_one_two = number_two
if higher_of_one_two > number_three:
    highest_number = higher_of_one_two
elif number_three > higher_of_one_two:
    highest_number = number_three

print(f"The max number is {highest_number}")
