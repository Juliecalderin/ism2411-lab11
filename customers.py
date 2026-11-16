# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Update and add
customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: no email key in this customer")

# Exercise 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping without .items() only gives you the keys, not the values.
# .items() gives you each key AND its value together, so you can print both.
for key in customer:
    print(key)

# Exercise 5: Lookup table
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

discount = tier_discounts.get(customer["tier"], 0)
purchase = 200
final_price = purchase * (1 - discount)

print("Tier:", customer["tier"])
print("Discount:", f"{discount:.0%}")
print("Final price:", f"${final_price:.2f}")
