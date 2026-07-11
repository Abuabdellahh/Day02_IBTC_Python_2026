# Day 02 - Practice Exercisesexercises 
# IBT 2026 Python Bootcamp
# ============================================================


# ----------------------------------------------------------
# Exercise 1: Temperature Label
# if / elif / else — check the weather in Addis Ababa today
# ----------------------------------------------------------

temp = float(input("Enter today's temperature in °C: "))

if temp < 15:
    label = "cold"
elif temp <= 28:
    label = "warm"
else:
    label = "hot"

print(f"At {temp}°C it feels {label} outside.")


# ----------------------------------------------------------
# Exercise 2: Receipt Loop
# for loop + range — print receipt numbers 1 through 10
# ----------------------------------------------------------

print("\n--- Daily Receipts ---")
for n in range(1, 11):
    print(f"Receipt #{n}")


# ----------------------------------------------------------
# Exercise 3: Even Numbers
# Loop + modulo — every even number from 1 to 20
# ----------------------------------------------------------

print("\n--- Even Numbers (1–20) ---")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


# ----------------------------------------------------------
# Exercise 4: Discount Function
# apply_discount(price, percent=10) — ETB prices
# ----------------------------------------------------------

def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    final_price = price - discount_amount
    return final_price


print("\n--- Discount Calculator ---")

original_price = 850  # ETB

# With default 10 % discount
discounted = apply_discount(original_price)
print(f"Original price:          {original_price} ETB")
print(f"After 10% discount:      {discounted} ETB")

# With a custom 25 % discount
discounted_25 = apply_discount(original_price, 25)
print(f"After 25% discount:      {discounted_25} ETB")


# ----------------------------------------------------------
# Exercise 5: Countdown
# while loop — count down from 5 to 1 then "Liftoff!"
# ----------------------------------------------------------

print("\n--- Countdown ---")
count = 5
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")
