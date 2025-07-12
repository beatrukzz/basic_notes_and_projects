#match-case statements (switch): An alternative to using
#                                using if-else statements
#                                executes some code if a value matches a "case"
#                                benifits: cleaner and syntax is more readable

day = int(input("Enter a day number (0-6): "))
def day_of_week(day):
    match day:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case _:
            return "Invalid day number"

print(f"The day is: {day_of_week(day)}")

# | means 'OR'
