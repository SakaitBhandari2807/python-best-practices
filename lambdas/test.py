l = [1, 2, 3, 4, 5]


# TODO 1: Multiply the list item by 2 using lambda function
def multiplyBy2(num):
    return num * 2


print(list(map(multiplyBy2, l)))
print(list(map(lambda x:x*2, l)))

# TODO 2: Unpacking arguments


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total


def calculator(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        raise "No valid operator provided"


print(multiply(1,2,3,4,5))
print(calculator(1,2,3,4,5, operator="*"))


# TODO 3: keywords or named arguments
def show(**kwargs):
    print(kwargs)

def prettyshow(**kwargs):
    show(**kwargs)
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k}: {v}")

student = {
    'name' : 'Divyanshu','age': 25
}

prettyshow(**student)

