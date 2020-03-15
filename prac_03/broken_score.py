"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 0 and score < 50:
        return "This score is Bad"
    elif score >= 50 and score < 90:
        return "This score is Passable"
    elif score >= 90 and score <= 100:
        return "This score is excellent"
    else:
        return "Error"


main()
