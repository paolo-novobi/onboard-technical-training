def listfunc4(a,n):
    # return a list of n starting elements and n ending elements of list a
    if (n < 0):
        print("The number of elements have to be greater than 0")
        return []
    m = len(a)/2
    if (m<=n):
        return a

    return a[0:n]+a[-n:]


if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print("Given the following list : ")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a)

    result = listfunc4(a,1)
    print("The list of first and last element: "+str(result))
    result = listfunc4(a,3)
    print("The list of first 3 and last 3 elements : "+str(result))
    result = listfunc4(a,8)
    print("The list of first 8 and last 8 elements : "+str(result))
