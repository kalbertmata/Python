# 1.1. Hello World (again) (3 points)

def name_function():
    name = input("Enter your name: ")
    print("hello", name)


name_function()

# 1.2. Dog Years (3 points)


def dog_function():
    dog_age_h = int(input("Enter your dog's age: "))
    dog_age_d = dog_age_h * 7
    print("your dog is,", dog_age_h, "human years to", dog_age_d, "dog years")


dog_function()


def items_function():
    items = input("Enter item or stop to end: ")
    while items != "stop":
        if items == "stop":
            items = "stop"
        else:
            print(items)
            items = input("Enter item or stop to end: ")


items_function()