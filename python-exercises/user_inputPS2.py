from datetime import date
from datetime import datetime
def userinputfunc():
    # asks the user to enter their name, their date of birth (mm/dd/yyyy), their gender, their address.
    username = input("Enter your name :")
    dateofbirth = input ("Enter your date of birth (mm/dd/yyyy):")
    gender = input("Input your gender :")
    address = input("Input your address :")

    today = date.today()
    birthdate = datetime.strptime(dateofbirth, '%m/%d/%Y').date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    print("   Available commands are: `name`, `age`, `dob`, 'gender`, `address`, `all`")
    command = input("What would you like to know?")
    match command:
        case 'name':
            print("Your name is :",username)
        case 'age':
            print("Your age is :",age)
        case 'dob':
            print("Your date of birth is :",dateofbirth)
        case 'gender':
            print("Your gender is :",gender)
        case 'address':
            print("Your address is :", address)
        case 'all':
            print("Your name is :",username)
            print("Your age is :",age)
            print("Your date of birth is :",dateofbirth)
            print("Your gender is :",gender)
            print("Your address is :", address)
        case _:
            print ("The command  ot found")

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = userinputfunc()
