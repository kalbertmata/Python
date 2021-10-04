def format_name(first_name, last_name):
    return first_name + " " + last_name


first = input("What is your first name: ")
last = input("What is your last name: ")
print("Hello", format_name(first, last))


def average(num1, num2, num3):

    sum = num1 + num2 + num3
    avg = sum/3
    return avg


print(average(5, 15, 5))


def my_func(num1, num2):
    if num1 < 0:
        return
    else:
        return num1 + num2 * 2


print(my_func(20, 20))


def prrint_dict(dict):
    keys = list(dict.keys())
    values = list(dict.values())

    for i in range(0, len(keys)):
        k = keys[i]
        v = values[i]
        print(k, v)

simple_dict= {
    "name": "Thor",
    "age": "25"
}

prrint_dict(simple_dict)


def sum_two_number(a, b):
    return a + b


number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))


def multiply_by(a, b=2, p_value=False):
    if p_value:
        print("a,b id=s equal to", a, b)
    return a * b


print(multiply_by(2))
print(multiply_by(2, 10, True))


print(multiply_by(2))


def func(*args):
    print(type(args))
    print(args)

func("a","b","c","d","e")

def func1(**kwargs):
    print(kwargs)

func1(a=1, b=2, c=3)


# this is server side
def db_connect(**options):
    conn_string = {
        "host" : options.get("host", "127.0.0.1"),
        "port" : options.get("port", 5432),
        "user": options.get("user", "admin"),
        "pwd": options.get("pwd", ""),
        "catalog": options.get("catalog", "default_db")
    }
    print(conn_string)
 # client side
db_connect(host="192.0.0.1",port="122002",user="Admin",pwd="ItsSecret" )

