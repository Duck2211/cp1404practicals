from prac_06.guitar import Guitar

guitars = []


def main():
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.", end="\n\n")
        name = input("Name: ")

    print("These are my guitars:")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("guitar sort result:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(
                "Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars so Quick, go and buy one")

main()
