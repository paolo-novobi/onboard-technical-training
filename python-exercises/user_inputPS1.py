from datetime import date

def userinputfunc():
    
    # asks the user to enter their name and their age.
    username = input("Enter your name :")
    userage = input("Enter your age :")

    # Print out a message tells them the year that they will turn 100 years old
    today = date.today()
    year100 = today.year + (100-int(userage))
    print(username + ", the year when you will turn 100 years old :" + str(year100))

    # Ask users how many times they would like the above message to display
    numtimes = input("How many times you would like the above message to display: ")
    for i in range(int(numtimes)):
        print(username + ", the year when you will turn 100 years old :" + str(year100)+"\n")

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = userinputfunc()

