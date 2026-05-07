print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? Rs."))
tip = int(input("What is the tip percentage you would like to give?10,12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip/100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: Rs.{final_amount}")