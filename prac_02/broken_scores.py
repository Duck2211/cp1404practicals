def main():
    score = float(input("Enter score: "))
    grades = determine_score(score)
    print(grades)
    import random
    print(f"The random score is", determine_score(random.randint(0, 100)))


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


main()
