"""
algorithm:
get sales
while sales >=0:
 if sales < 1000
    sales_bonus = sales * 0.1
 else
    sales_bonus = sales * 0.15
 display sales_bonus
display "thank u for using this"
"""
sales = float(input("enter sales $: "))
while sales >=0:
 if sales < 1000:
    sales_bonus = sales * 0.1
 else:
    sales_bonus = sales * 0.15
 print(f"sales bonus is {sales_bonus}")
print("thank u for using this")