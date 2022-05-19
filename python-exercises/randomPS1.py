import random

def randomfunc():
    # Let the user do until they type 'exit'
    guessword =''
    while True:
        guessword = input ("Guess a number (Enter exit to quit) : ")
        if (guessword != "exit"):
            randomnum = random.randint(1,9)
            times = 1
            while (int(guessword) != randomnum):
                if (int(guessword)>randomnum):
                    print("Your guess is too high!")
                else:
                    print("Your guess is too low!")
                times = times +1
                guessword = input('Please guess again: ')
            print("You are exactly right. You have guessed "+ str(times) + " times")
        else:
            break

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = randomfunc()
