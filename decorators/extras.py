def func():
    return 1


def wrapper(new_func):
    print('wrapper inside')

    def secret():
        print("inside secret")
        new_func()
        print("going outside secret")
    return secret


@wrapper
def sum():
    print("I calculate sum")


sum()
# testing = wrapper(sum)
# testing()


