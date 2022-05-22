def listfunc2():
    # Given the following list, print out all the elements in ascending order
    print("Given the list: [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]")
    a = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
    a.sort()
    print("The list is sorted: ",a)
    # and print out 2 separate lines, one is for even numbers and the other is for odd numbers.
    evennums = filter(lambda element: element%2 ==0, a)
    oddnums = filter(lambda element: element%2 !=0, a)
    print("The list of even numbers : ",list(evennums))
    print("The list of odd numbers : ",list(oddnums))

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = listfunc2()
