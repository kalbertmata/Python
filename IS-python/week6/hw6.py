# Exercise #1: (6 points)

try:

    # open a file for reading
    file_var =  open("most_popular_words_in_english.txt", "r")
    my_var = input("Enter a word in english ")
    file_r = file_var.read()

    if my_var in file_r:
        print("Good job!")
    else:
        print("Sorry")
# an error occurred!  handle it here
except:
    print ("Something went wrong!")

