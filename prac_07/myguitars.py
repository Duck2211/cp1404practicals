import csv
from prac_06.guitar import Guitar



def main():
    guitars = []
    class_guitars = []
    new_guitar = []

    with open('guitars.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skip header row
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        class_guitars.append(guitar)
    class_guitars.sort()
    for i, guitar in enumerate(class_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.", end="\n\n")
        name = input("Name: ")

    with open("guitars.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars + new_guitar:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print("New guitar(s) added to the file")


main()
