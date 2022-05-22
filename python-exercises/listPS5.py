def listfunc5(a):
    unique_list = []
    # traverse all elements
    for x in a:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def listfunc6(a):
    # Write a function that takes a list and returns a new list that contains all the unique elements of the list.
    # using set
    alist = list(set(a))
    return alist


if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print("Given the following list : ")
    a = [1, 1, 2, 3, 5, 34, 55, 8, 13, 21, 34, 55, 89]
    print(a)

    result = listfunc5(a)
    print ("The unique list of the above list using loop : "+str(result))
    result = listfunc6(a)
    print ("The unique list of the above list using set : "+str(result))
