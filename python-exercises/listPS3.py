def listfunc3(a,b):
    # find the common elements of two given lists
    a_set = set(a)
    b_set = set(b)
    resultlist = list(a_set.intersection(b_set))
    resultlist.sort()
    return resultlist

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print("Given the following two lists : ")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(a)
    print(b)
    result = listfunc3(a,b)
    print ("The common elements of the above lists : "+str(result))
