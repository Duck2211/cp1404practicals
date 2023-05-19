from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxi_lists = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    taxi_pick = None
    current_bill = 0
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            show_taxi()
            taxi_pick = processing_taxi_choice()
            if taxi_pick is not None:
                taxi_lists[taxi_pick].start_fare()
        elif choice == "d":
            if taxi_pick is None:
                print("You need to choose a taxi before u can drive")
            else:
                distance_travel = int(input("Drive how far?"))
                taxi_lists[taxi_pick].drive(distance_travel)
                print(f"Your {taxi_lists[taxi_pick].name} trip gonna cost you {taxi_lists[taxi_pick].collect_fare()}")
                current_bill += taxi_lists[taxi_pick].collect_fare()
        else:
            print("Invalid input")
        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: {current_bill}")
    show_taxi()

def show_taxi():
    """This function will display the taxi list"""
    print("Taxi avaliable:")
    for i in range(0, len(taxi_lists)):
        print(f"{i}- {taxi_lists[i]}")


def processing_taxi_choice():
    """this will process the taxi choices if it's valid or not"""
    choice = input("Taxis Available:")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > len(taxi_lists) - 1:
        choice = input("choose taxi")
    return int(choice)


main()
