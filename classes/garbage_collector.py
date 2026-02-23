import weakref


def bye():
    print("...deleting the object")

s1 = {1,2,3}

print(type(s1))

s2 = s1

ender = weakref.finalize(s1, bye)

print(ender.alive)

del s1
print(ender.alive)

s2 = "spam"
print(ender.alive)