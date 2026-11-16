# Reflection
#
# Q1: In Exercise 3 you saw the difference between .get() and bracket notation.
# When in real work would you use each one, and what's your rule of thumb?
# I use .get() when a key might be missing, like optional customer info such as
# an email or phone number, because it returns a default instead of crashing.
# I use bracket notation when the key must exist, like a required ID, because
# I want the KeyError to show me right away that something is wrong.
# My rule of thumb: .get() if missing is normal, brackets if missing is a bug.
#
# Q2: Exercise 8 built a summary dictionary with a loop. What does this remind
# you of from Excel, and why might Python be more useful for large datasets?
# It reminds me of a pivot table or a SUMIF, where you add up amounts for each
# category like region. Python is more useful for large datasets because it
# handles millions of rows without slowing down or freezing like a spreadsheet.
# It is also repeatable, so I can rerun the same code on new data.

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

# Exercise 6: List of dicts
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Carla", "tier": "silver"}
]

for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    amount = 300 * rate
    print(f"{c['name']} | {c['tier']} | discount: ${amount:.2f}")

# Exercise 7: Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")

# Exercise 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
