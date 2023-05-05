"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    amount_of_months = int(input("How many months? "))

    for amount_of_months in range(1, amount_of_months + 1):
        income = float(input("Enter income for month " + str(amount_of_months) + ": "))
        incomes.append(income)

    report(amount_of_months, incomes)


def report(amount_of_months, incomes):
    """Display the report of the income and the total of income of all the months"""
    print("\nIncome Report\n-------------")
    total = 0
    for amount_of_months in range(1, amount_of_months + 1):
        income = incomes[amount_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(amount_of_months, income, total))


main()