print("Welcome to the tip calculator!")
total_bill_string = input("What was the total bill?")
tip_percentage_string = input("What percentage tip would you like to give? 10, 12 or 15?")
number_of_people_string = input("How many people to split the bill")

total_bill = float(total_bill_string)
tip_percentage = int(tip_percentage_string)
number_of_people = int(number_of_people_string)

should_pay = (total_bill * (1 + tip_percentage / 100)) / number_of_people

# print("Each person should pay: $" + str(round(should_pay, 2)))
print(f"Each person should pay: $ {round(should_pay, 2)}")

