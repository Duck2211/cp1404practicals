def main():
    print("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result=celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} C")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit:"))
            result=fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option")
        print("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    result = celsius * 9.0 / 5 + 32
    return result


def fahrenheit_to_celsius(fahrenheit):
    result = 5 / 9 * (fahrenheit - 32)
    return result


main()
