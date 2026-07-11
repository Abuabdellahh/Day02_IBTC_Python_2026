# TeleBirr Tip Calculator

bill_total = 10000
friends = 5

customers = ["Kidus", "Kalab", "Abel", "Ephrem", "Simon"]

def split_bill(total, friends, tip_rate=0.10):
    tip = total * tip_rate
    total_with_tip = total + tip
    print(f"Waiter complaining for the small amount of tip he got: {tip} ETB")
    return total_with_tip / friends

split = split_bill(bill_total, friends)

print(f"Total Bill: {bill_total} ETB")
print(f"Total with tip: {bill_total + (bill_total * 0.10)} ETB")
print(f"Each friend will pay: {split} ETB")

for customer in customers:
    print(f"{customer} will pay: {split} ETB")