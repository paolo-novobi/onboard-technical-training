from datetime import date
from datetime import datetime
import pytz

def datetimefunc():
    # Get the current date, datetime and print out to the screen
    today = date.today()
    print("Exercise 1 : ")
    print("Current date: ",today)
    cdatetime = datetime.now()
    print("Current datetime: ",cdatetime)

    # Get the current datetime of the timezone GMT +7 and convert it into UTC, GMT and print out to the screen
    print("\nExercise 2 : ")
    now = datetime.now(pytz.timezone('Etc/GMT+7'))
    print("Current Time of the timezone GMT+7 =", now)
    print("Converted time in UTC: ", now.astimezone(pytz.timezone('UTC')))
    print("Converted time in GMT: ", now.astimezone(pytz.timezone('GMT')))

    # Convert the following date string into date and print out as following format dd/mm/yyyy
    print("\nExercise 3 : ")
    datefstr = datetime.strptime("2021-07-04","%Y-%m-%d")
    out = datefstr.strftime("%d/%m/%Y")
    print(out)

    # current_time = now.strftime("%H:%M:%S")
if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = datetimefunc()
