# # splitter app

def bill_splitter():

    print("Welcome to the Bill Splitter App!!")

try:
    total_bill = float(input("Enter total bill amount: "))
    num_people = int(input("Enter number of people: "))
    tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))
except ValueError:
    print("Invalid input! Please enter numbers only.")

else:

    tip_amount = total_bill * (tip_percentage / 100)
    total_bill_with_tip = total_bill + tip_amount
    per_person_bill = total_bill_with_tip / num_people

    print(f"Tip Amount: {tip_amount}")
    print(f"Total Bill (with Tip): {total_bill_with_tip}")
    print(f"Each person should pay: {per_person_bill}")

while True:

    print("Thank You....")

    choice = input("Would you like to calculate another bill? (Y/n):")

if choice() == 'y':

        print("Thank you!")

        

