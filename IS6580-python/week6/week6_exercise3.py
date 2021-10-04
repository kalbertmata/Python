#1. Exception handling (5 points)

while True:
    try:
        integer_input= input("Enter a number")
        if integer_input.isdecimal():
            break
    except:
        print("not an int")

#2. File IO (5 points)


while True:
    file = input("Enter a file name: ")
    try:
        file_g = open(file,"a")
        while True:
            text= input("What do you want to write? done")
            if text.lower()== "done":
                break
            file_g.write(text+"\n")

            try:
                file_g.close()
            except:
                pass
    except Exception as ex:
        print(ex)

    else:
        break
#3. Name (5 points)



try:
    file = input("Enter a file name: ")
    file_g = open(file, "r")
    contents = file_g.read()
    print(contents)
except:
    print("lol")
