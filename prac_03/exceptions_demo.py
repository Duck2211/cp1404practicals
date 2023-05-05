"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
only happen when u type something for numerator and denominator that isn't a number
2. When will a ZeroDivisionError occur?
when u put denominator as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Adding while loop to validate the number to prevent the zero division error
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


