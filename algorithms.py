# start of Question 1
# get user input
entered_number_string = input(print("Enter a number and find the sum from 1 to the entered number"))
# change str to int
entered_number_int = int(entered_number_string)
# variable for loop counter and for the sum
loop_counter = 1
total = 0
# loop counter is added to sum until the loop condition is complete
while entered_number_int >= loop_counter:
    total = total + loop_counter
    loop_counter = loop_counter + 1

# prints sum of the loop
print(f"The sum is {total}")


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

