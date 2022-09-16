# Name: Lucas Kolb
# Class: ISQA 3900 Web Application Development
# HW:Activity 3
# Date: 09/10/2022
# -------------------------------------------------------------------------
def main():
    def display_title():
        print("Welcome to the Grade Calculator")
    display_title()
    def get_totalPoints():
        points = float(input("Enter the total score (0-1000): "))

        if points < float(0):
            print("You must enter integer values >= 0 and <= 1000. Try again.")
            get_totalPoints()
        elif points > float(1000):
            print("You must enter integer values >= 0 and <= 1000. Try again.")
            get_totalPoints()
        else:
            grade = points / 10
            def get_letterGrade():
                if grade < float(60):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: F")
                elif grade == float(60) or grade <= float(69.99):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: D")
                elif grade == float(70) or grade <= float(77.99):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: C")
                elif grade == float(78) or grade <= float(81.99):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: C+")
                elif grade == float(82) or grade <= float(87.99):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: B")
                elif grade == float(88) or grade <= float(91.99):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: B+")
                elif grade == float(92) or grade <= float(100.00):
                    print("You earned an average of", round(float(grade), 2), "%. Letter grade earned: A")
                restart = input("Would you like to enter another score (y/n)?")
                if restart.upper() == "Y":
                    get_totalPoints()
                elif restart.upper() == "N":
                    print("have a nice day.")
                else:
                    print("Err, please try again")
                    get_letterGrade()
            get_letterGrade()
    get_totalPoints()
main()