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
