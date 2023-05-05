def main():
    print("(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit\n")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = validating()
        elif choice == "P":
            grades = determine_score(score)
            print(grades)
        elif choice == "S":
            stars(score)
        else:
            print("Invalid Choice")
        print("(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit\n")
        choice = input(">>>").upper()
    print("Thank u for using this")


def validating():
    score = int(input("score:"))
    while score < 0 or score > 100:
        print("invalid score")
        score = int(input("score:"))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"


def stars(score):
    print("*" * score)


main()
