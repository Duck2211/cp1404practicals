"""
algorithm:
total = 0
get amount_items
while amount_items < 0:
    display "invalid amount"
    get amount_items
for i in range(amount_items)
    get price_items
    total += price_items
if total > 100
    total *= 0.9
display amount_items, total

"""
total = 0
amount_items = int(input("number of items:"))
while amount_items < 0:
    print("invalid amount")
    amount_items = int(input("number of items:"))

for i in range(amount_items):
    price_items = float(input("price of item:"))
    total += price_items

if total > 100:
    total *= 0.9
print(f"total price for {amount_items} item is ${total:.2f}")
