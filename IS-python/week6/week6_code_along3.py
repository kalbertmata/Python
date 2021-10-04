# code 3

while True:
    file = input("Enter a file name: ")
    try:
        file_g = open(file,"a")
        contents = file_g.read()
        print(contents)
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


