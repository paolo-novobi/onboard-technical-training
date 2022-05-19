from collections import Counter

def stringfilefunc():
    # open the file and read lines without newlines
    file = open("text.txt","r")
    lines = file.read().splitlines()
    file.close()

    # concatenate the lines into text
    text = ""
    for line in lines:
        text = text + " " + line

    tokcounts = dict(Counter(text.split()))

    # save the words with multiple occurences into file
    file1 = open("multipleoccurences.txt", "w")
    mtexts = ""
    for key, value in tokcounts.items():
        if value>1:
            mtexts = mtexts + key + ","
    mtexts = mtexts[0:len(mtexts)-1]
    file1.write(mtexts)

    # print out the count of appearences for each word
    print("The words and number of appearances in the text are as follows: ")
    for key, value in tokcounts.items():
        print(key + " : " + str(value))

    # allow user to input a word, check if the word is in the file.
    # If yes, print the times that the word appear, or print out a message saying it does not exist if no.
    print("\n")
    searchword = input("Please enter the word that you are searching: ")
    if searchword in tokcounts.keys():
        print("The word '" + searchword + "' appeared " + str(tokcounts[searchword]) +" (time/times) in the text")
    else:
        print("The word '" + searchword + "' does not exist ")

    # print the first 100 characters of the text
    print("\nThe first 100 chatacters of the text is: ", text[0:100])


if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    result = stringfilefunc()

