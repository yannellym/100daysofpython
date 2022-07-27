#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
name = input("What's your name?")
print(f"Hi {name}, Welcome to my tip calculator!")
bill_total = float(input("What is the total of amount of the bill?"))
tip = int(input("How much tip would you like to give? 5 10 15 20?"))
tip_of_bill = bill_total * (tip/100)
bill_with_tip = bill_total + tip_of_bill
amount_of_people = int(input("How many people to split the bill?"))
final_amount = int(bill_with_tip / amount_of_people)
print("{:.2f}".format(final_amount))
