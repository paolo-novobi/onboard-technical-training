import random
import string

# characters to generate password from
characters = list(string.ascii_letters + string.digits + "()!#%^$&*@?")

def randompasswordfunc():
    # ask user to provide password
    passlen = input("Enter the desired password length: ")

    # picking random characters from the list
    password = []
    for i in range(int(passlen)):
        # shuffling the characters and choose one
        random.shuffle(characters)
        password.append(random.choice(characters))

    # shuffling the generated password
    random.shuffle(password)

    # printing the password
    print("".join(password))

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = randompasswordfunc()
