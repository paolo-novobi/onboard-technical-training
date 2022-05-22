
def listfunc1():
    # Given the following list, print out all the elements that are less than 15 one by one
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Given this list: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]")
    print("Printing all elements that < 15 one by one")
    for i in a:
        if (i<15):
            print(i)

    # store the elements < 15 in a list and print out the list
    print("Printing all elements that < 15 using a stored list")
    b = [i for i in a if i<15]
    print(b)

    # Given a threshold and print the list of elements smaller than the threshold
    threshold = input("Given a threshold for the elements : ")
    print("List of elements smaller than "+ threshold)
    b = [i for i in a if i<int(threshold)]
    print(b)

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = listfunc1()
